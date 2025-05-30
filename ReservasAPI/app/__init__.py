from flask import Flask, jsonify
from flasgger import Swagger
from .extensions import db
from .config import DATABASE_URI, TRACK_MODIFICATIONS
from .controllers.reserva_controller import reserva_bp

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = TRACK_MODIFICATIONS
    app.config["SWAGGER"] = {
        "title": "Reservas API - Documentação Swagger",
        "uiversion": 3
    }

    db.init_app(app)
    Swagger(app)
    app.register_blueprint(reserva_bp, url_prefix="/reservas")

    @app.route('/')
    def home():
        return '''
            <!DOCTYPE html>
            <html lang="pt-br">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>DevAPI</title>
                <style>
                    body {
                        margin: 0;
                        padding: 0;
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        background: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        text-align: center;
                        color: #333;
                    }
                    h1 {
                        font-size: 2.5em;
                        color: #1e88e5;
                        margin: 0.2em 0;
                    }
                    p {
                        font-size: 1.1em;
                        margin: 0.3em 0;
                    }
                    .info {
                        color: #666;
                        font-weight: bold;
                    }
                    a {
                        background-color: #1e88e5;
                        color: white;
                        padding: 10px 20px;
                        border-radius: 6px;
                        text-decoration: none;
                        font-size: 1em;
                        box-shadow: 0 3px 6px rgba(0,0,0,0.1);
                        transition: background-color 0.3s ease, transform 0.2s ease;
                        margin-top: 0.5em;
                    }
                    a:hover {
                        background-color: #1565c0;
                        transform: scale(1.03);
                    }
                    .emoji {
                        font-size: 1.8em;
                        margin-bottom: 0.2em;
                    }
                </style>
            </head>
            <body>
                <div class="emoji">🚀</div>
                <h1>Bem-vindo à <strong>DevAPI</strong></h1>
                <p>Explore nossa documentação e conheça os endpoints disponíveis.</p>
                <a href="/apidocs/">👉 Acessar Swagger Docs</a>
            </body>
            </html>
        '''


    with app.app_context():
        db.create_all()

    return app
