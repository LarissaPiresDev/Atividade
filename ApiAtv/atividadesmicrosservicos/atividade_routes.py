from flask import Blueprint, jsonify, request
from .atividade_model import AtividadeNaoEncontrada, IdNaoInteiro, IdMenorqueUm, listar_atividades, listar_atividades_por_id
from config import db
import requests

schoolSystem = 'http://127.0.0.1:5003'

atividades = Blueprint('atividades', __name__)

def validar_professor(professor_id):
    resp = requests.get(f"{schoolSystem}/turmas/{professor_id}")
    return resp.status_code == 200

@atividades.route('/atividades', methods=['GET'])
def get_atividades():
    return jsonify(listar_atividades())

@atividades.route('/atividades/<id>', methods=['GET'])
def getPorId(id):
    try:
        atividade = listar_atividades_por_id(id)
        return jsonify(atividade)
    except IdNaoInteiro:
        return jsonify({'mensagem': 'Id Incorreto!!! Valor de id precisa ser um número Inteiro'}), 400
    
    except IdMenorqueUm:
        return jsonify({'mensagem': 'O valor de Id precisa ser maior que Zero'}), 400
    
    except AtividadeNaoEncontrada:
        return jsonify({'mensagem': 'Id de atividade NOT FOUND (Não Encontrado)'}), 404


@atividades.routes('/atividades', methods=['POST'])
def postAtividade():
    atividade = request.json
    
    
"""


@atividades('/<int:id_atividade>/professor/<int:id_professor>', methods=['GET'])
def obter_atividade_para_professor(id_atividade, id_professor):
    try:
        atividade = atividade_model.obter_atividade(id_atividade)
        if not PessoaServiceClient.verificar_leciona(id_professor, atividade['id_disciplina']):
            atividade = atividade.copy()
            atividade.pop('respostas', None)
        return jsonify(atividade)
    except atividade_model.AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404 """
