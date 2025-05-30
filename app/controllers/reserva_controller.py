from flask import Blueprint, request, jsonify
from flasgger import swag_from
from ..models.reserva import Reserva

reserva_bp = Blueprint("reserva", __name__)

@reserva_bp.route("/", methods=["GET"])
@swag_from({
    'tags': ['Reserva'],
    'description': 'Lista todas as reservas registradas.',
    'responses': {
        200: {
            'description': 'Lista de reservas obtida com sucesso.',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'turma_id': {'type': 'integer'},
                        'aluno_nome': {'type': 'string'},
                        'sala': {'type': 'string'},
                        'horario': {'type': 'string'},
                        'data_reserva': {'type': 'string'}
                    }
                }
            },
            'examples': {
                'application/json': [
                    {
                        'id': 1,
                        'turma_id': 1,
                        'aluno_nome': 'Gabryel',
                        'sala': 'Lab 1',
                        'horario': '08:00:00',
                        'data_reserva': '2025-05-29'
                    }
                ]
            }
        }
    }
})
def listar():
    reservas = Reserva.listar()
    return jsonify([r.to_dict() for r in reservas]), 200


@reserva_bp.route("/", methods=["POST"])
@swag_from({
    'tags': ['Reserva'],
    'description': 'Cria uma nova reserva de sala.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'turma_id': {'type': 'integer', 'example': 1, 'description': 'ID da turma'},
                    'aluno_nome': {'type': 'string', 'example': 'Gabryel', 'description': 'Nome do aluno'},
                    'sala': {'type': 'string', 'example': 'Lab 1', 'description': 'Sala para reserva'},
                    'horario': {'type': 'string', 'example': '08:00', 'description': 'Horário no formato HH:MM'},
                    'data_reserva': {'type': 'string', 'format': 'date', 'example': '2025-05-29', 'description': 'Data no formato YYYY-MM-DD (opcional)'}
                },
                'required': ['turma_id', 'aluno_nome', 'sala', 'horario']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Reserva criada com sucesso.',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'turma_id': {'type': 'integer'},
                    'aluno_nome': {'type': 'string'},
                    'sala': {'type': 'string'},
                    'horario': {'type': 'string'},
                    'data_reserva': {'type': 'string'}
                }
            },
            'examples': {
                'application/json': {
                    'id': 1,
                    'turma_id': 1,
                    'aluno_nome': 'Gabryel',
                    'sala': 'Lab 1',
                    'horario': '08:00:00',
                    'data_reserva': '2025-05-29'
                }
            }
        },
        400: {
            'description': 'Dados inválidos.',
            'examples': {
                'application/json': {
                    'erro': 'Formato inválido para data ou horário. Use HH:MM:SS e YYYY-MM-DD'
                }
            }
        },
        500: {
            'description': 'Erro interno no servidor.',
            'examples': {
                'application/json': {
                    'erro': 'Erro interno no servidor'
                }
            }
        }
    }
})
def criar():
    dados = request.get_json()

    try:
        reserva = Reserva.criar(dados)
        return jsonify(reserva.to_dict()), 201

    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

    except Exception:
        return jsonify({"erro": "Erro interno no servidor"}), 500


@reserva_bp.route("/<int:id>", methods=["DELETE"])
@swag_from({
    'tags': ['Reserva'],
    'description': 'Deleta uma reserva existente pelo ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da reserva que será deletada'
        }
    ],
    'responses': {
        200: {
            'description': 'Reserva deletada com sucesso.',
            'examples': {
                'application/json': {
                    'mensagem': 'Reserva deletada com sucesso'
                }
            }
        },
        404: {
            'description': 'Reserva não encontrada.',
            'examples': {
                'application/json': {
                    'erro': 'Reserva não encontrada'
                }
            }
        },
        500: {
            'description': 'Erro interno no servidor.',
            'examples': {
                'application/json': {
                    'erro': 'Erro interno no servidor'
                }
            }
        }
    }
})
def deletar(id):
    try:
        sucesso = Reserva.deletar(id)
        if sucesso:
            return jsonify({"mensagem": "Reserva deletada com sucesso"}), 200
        return jsonify({"erro": "Reserva não encontrada"}), 404
    except Exception:
        return jsonify({"erro": "Erro interno no servidor"}), 500
