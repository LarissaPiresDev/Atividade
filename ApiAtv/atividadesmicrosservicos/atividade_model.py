from config import db
class Atividades(db.Model):
    __tablename__ = 'atividade'

    id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(db.Integer, nullable=False)
    enunciado = db.Column(db.String(250), nullable=False)
    alternativas = db.Column(db.Text, nullable=False)
    resposta = db.Column(db.String(1), nullable=False)


    def __init__(self, professor_id, enunciado, alternativas, resposta):
        self.professor_id = professor_id
        self.enunciado = enunciado
        self.alternativas = alternativas
        self.resposta = resposta
        
    def exibir_atividade(self):
        return {"1- id": self.id, 
                "2- professor_id": self.professor_id, 
                "3- enunciado": self.enunciado, 
                "4- alternativas": self.alternativas.split(' | ')}
    
class IdNaoInteiro(Exception):
    pass
class IdMenorqueUm(Exception):
    pass
class AtividadeNaoEncontrada(Exception):
    pass
    
def listar_atividades():
    atividades = Atividades.query.all()
    return [atividade.exibir_atividade() for atividade in atividades]

def listar_atividades_por_id(id):
    try:
        id = int(id)
    except ValueError:
        raise IdNaoInteiro
    if id <=0:
        raise IdMenorqueUm
    
    atividade = Atividades.query.get(id)
    if not atividade:
        raise AtividadeNaoEncontrada
    return atividade.exibir_atividade()

def criar_atividade(atividade):

    alternativas_formatadas = ' | '.join(atividade['alternativas'])
    new_atividade = Atividades(
        professor_id= int(atividade['professor_id']),
        enunciado= str(atividade['enunciado']),
        alternativas=str(alternativas_formatadas),
        resposta=str(atividade['resposta'])
    )

    db.session.add(new_atividade)
    db.session.commit()
    return new_atividade.exibir_atividade()


    
