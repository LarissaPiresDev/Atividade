from config import app, db
from atividadesmicrosservicos.atividade_routes import atividades

app.register_blueprint(atividades)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port = app.config['PORT'], debug = app.config['DEBUG'])
