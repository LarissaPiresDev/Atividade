from flask import Blueprint, jsonify, request
from .atividade_model import AtividadeNaoEncontrada, IdNaoInteiro, IdMenorqueUm, listar_atividades, listar_atividades_por_id, criar_atividade
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


@atividades.route('/atividades', methods=['POST'])
def postAtividade():
    atividade = request.json
    chaves_esperadas = {"professor_id", "enunciado", "alternativas", "resposta"}
    chaves_inseridas = set(atividade.keys())

    chaves_invalidas = chaves_inseridas - chaves_esperadas
    if chaves_invalidas:
        return jsonify({'mensagem': 'Chaves inseridas inválidas, retire-as',
                        'Chaves Esperadas': list(chaves_esperadas),
                        'Chaves Inválidas Inseridas': list(chaves_invalidas)
                        }), 400
    
    if set(chaves_esperadas) - set(chaves_inseridas):
        return jsonify({'mensagem': f'Para criar atividade, preciso que insira o valor os seguintes campos: {list(chaves_esperadas)}'}), 400

    if not isinstance(atividade['professor_id'], int) or atividade['professor_id'] <= 0:
        return jsonify({'mensagem': 'Campo "professor_id" PRECISA SER UM NÚMERO INTEIRO MAIOR DO QUE ZERO!!!'}), 400
    
    professor_id = atividade.get("professor_id")
    if not validar_professor(professor_id):
        return jsonify({'mensagem': 'Id de Professor Não Encontrado'}), 400

    if not isinstance(atividade['enunciado'], str) or not atividade['enunciado'].strip():
        return jsonify({'mensagem': 'O campo para a chave "enunciado" PRECISA SER UMA STRING E NÂO PODE ESTAR VAZIA!!!'}), 400
    
    if not isinstance(atividade['alternativas'], list) or len(atividade['alternativas']) < 2 or len(atividade['alternativas']) > 5 :
        return jsonify({'mensagem': 'O campo de "alternativas" PRECISA SER UMA LISTA [] COM PELO MENOS 2 OPÇÕES DE RESPOSTA e NO MÁXIMO 5!!!!'}), 400
    
    if not isinstance(atividade['resposta'], str) or not atividade['resposta'].strip():
        return jsonify({'mensagem': 'O campo de "resposta" PRECISA TER APENAS SER UMA STRING COM APENAS UMA LETRA COMO RESPOSTA (ex: a)'}), 400
    
    atividade['resposta'] = atividade['resposta'].strip().lower()
    if atividade['resposta'] not in ['a', 'b', 'c', 'd', 'e']:
        return jsonify({'mensagem': 'O campo de "resposta" PRECISA SER APENAS DA LETRA A até E'}), 400
    

    criar_nova_reserva = criar_atividade(atividade)
    return jsonify({'mensagem': 'Atividade Criada com Sucesso'})
        
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
