from datetime import datetime, date, time
from app.extensions import db
from sqlalchemy import Time


class Reserva(db.Model):
    __tablename__ = 'reservas'

    id = db.Column(db.Integer, primary_key=True)
    turma_id = db.Column(db.Integer, nullable=False)
    aluno_nome = db.Column(db.String(100), nullable=False)
    sala = db.Column(db.String(50), nullable=False)
    horario = db.Column(Time, nullable=False)  # Salva como horário mesmo
    data_reserva = db.Column(db.Date, default=date.today, nullable=False)  # Salva como data

    def to_dict(self):
        return {
            "id": self.id,
            "turma_id": self.turma_id,
            "aluno_nome": self.aluno_nome,
            "sala": self.sala,
            "horario": self.horario.strftime('%H:%M:%S'),  # Formata para string
            "data_reserva": self.data_reserva.strftime('%Y-%m-%d')  # Formata para string
        }

    @staticmethod
    def criar(dados):
        try:
            nova = Reserva(
                turma_id=dados["turma_id"],
                aluno_nome=dados["aluno_nome"],
                sala=dados["sala"],
                horario=datetime.strptime(dados["horario"], '%H:%M').time(),
                data_reserva=datetime.strptime(
                    dados.get("data_reserva", date.today().strftime('%Y-%m-%d')),
                    '%Y-%m-%d'
                ).date()
            )
            db.session.add(nova)
            db.session.commit()
            return nova
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Erro ao criar reserva: {e}")

    @staticmethod
    def listar():
        return Reserva.query.all()

    @staticmethod
    def deletar(id):
        reserva = Reserva.query.get(id)
        if reserva:
            db.session.delete(reserva)
            db.session.commit()
            return True
        return False
