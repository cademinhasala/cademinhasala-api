from app import db
#from sqlalchemy.dialects.postgresql import JSON

class Turma(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    disciplina = db.Column(db.String())
    #curso = db.Column(JSON)

    def __repr__(self):
        return '<id {}>'.format(self.id)