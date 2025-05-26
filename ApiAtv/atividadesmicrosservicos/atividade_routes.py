from flask import Blueprint, jsonify
from .atividade_model import listar_atividades
from config import db

schoolSystem = 'http://127.0.0.1:5003'

atividades = Blueprint('atividades', __name__)

@atividades.route('/atividades', methods=['GET'])
def get_atividades():
    return jsonify(listar_atividades())



""" @atividades.route('/atividade/<id>', methods=['GET'])
def obter_atividade(id_atividade):
    try:
        atividade = atividade_model.obter_atividade(id_atividade)
        return jsonify(atividade)
    except atividade_model.AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404


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
