
<h1 align="center">🏫 API RESTful com Flask - Gestão Escolar - Reservas de Salas</h1>

<p align="center">
   Microsserviço independente para controle de reservas de salas por turmas
</p>

## 📌 Sobre o Projeto

O **ReservasAPI** é um microsserviço RESTful autônomo, desenvolvido com **Python** e o framework **Flask**, com o objetivo de registrar e gerenciar **reservas de salas** feitas por turmas no contexto escolar. Ele segue a arquitetura **MVC**, utiliza o banco de dados **SQLite** e conta com integração ao **Swagger UI** para documentação interativa e testes das rotas.

#### 🗓️ Gerenciamento de Reservas
- Criação de reservas com os seguintes campos:
  - Nome do aluno
  - Turma
  - Sala
  - Data da reserva
  - Horário
- Validações obrigatórias para garantir integridade dos dados inseridos.

#### 📋 Listagem de Reservas
- Exibição completa de todas as reservas armazenadas no sistema.

#### 📄 Interface de Testes via Swagger UI
- Documentação interativa disponível para testar as rotas da API.
- Acesse em: [http://localhost:5001/apidocs](http://localhost:5001/apidocs)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python" />
  <img src="https://img.shields.io/badge/Flask-2.x-green?logo=flask" />
  <img src="https://img.shields.io/badge/Docker-ready-blue?logo=docker" />
  <img src="https://img.shields.io/badge/Postman-tested-orange?logo=postman" />
</p>

---

## 🎯 Objetivo

Desenvolver uma API RESTful com **Flask** para gerenciamento de reservas escolares de salas de aula. Faz parte do ecossistema de microsserviços escolares integrados via DevAPI.

---

## 📦 Clone ou Download

### 🔁 Clonar via Git
```bash
git clone https://github.com/SEU_USUARIO/ReservasAPI.git
```

### 📥 Download ZIP
1. Clique em `<> Code` > `Download ZIP`
2. Extraia o arquivo em seu computador

---

## 💻 Execução do Projeto

<details>
<summary><strong>📂 Acesse a pasta do projeto via terminal</strong></summary>

```bash
cd ReservasAPI
```

Ou clique com o botão direito na pasta do projeto e selecione **"Abrir no Terminal"**
</details>

<details>
<summary><strong>🔧 Instalar as dependências</strong></summary>

```bash
pip install -r requirements.txt
```
</details>

<details>
<summary><strong> 🔄 Rodar Projeto direto</strong></summary>

```bash
python -m app.main
```
</details>

**OU**

<details>
<summary><strong>🐳 Executar com Docker (recomendado)</strong></summary>

1. Criar a imagem Docker:
   ```bash
   docker build -t reservas-api .
   ```

2. Rodar o container:
   ```bash
   docker run -p 5001:5001 reservas-api
   ```

3. Acesse: [http://localhost:5001](http://localhost:5001)
</details>

---

## 🔄 Git Workflow

<details>
<summary><strong>🔃 Comandos de versionamento</strong></summary>

```bash
git add .
git commit -m "Descrição clara das mudanças"
git pull
git push origin main
```

> 📝 Substitua `main` pela sua branch se estiver em desenvolvimento.
</details>

---

## 👨‍💻 Equipe de Desenvolvimento

<table align="center">
  <tr>
    <td align="center" style="padding: 10px;">
      <a href="https://github.com/HenryModesto">
        <img src="Pictures/HENRYZ.jfif" width="200px" height="200px" style="border-radius: 8px;"/><br>
        <sub><b>HENRY MODESTO</b><br>2401244</sub>
      </a>
    </td>
    <td align="center" style="padding: 10px;">
      <a href="https://github.com/GabryelVenancio">
        <img src="Pictures/Cleffs.jpeg" width="200px" style="border-radius: 8px;"/><br>
        <sub><b>GABRYEL VENANCIO</b><br>2302495</sub>
      </a>
    </td>
    <td align="center" style="padding: 10px;">
      <a href="https://github.com/AndreyT1224">
        <img src="Pictures/ANDREW.jpeg" width="190px" style="border-radius: 8px;"/><br>
        <sub><b>ANDREY TOMAZ</b><br>2400729</sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/mauricio003">
        <img src="Pictures/Mauricio.jpg" width="120px;"/><br>
        <sub><b>MAURICIO COSTA</b><br>2400487</sub>
      </a>
    </td>
  </tr>
</table>

---

## 📁 Estrutura de Pastas

```
RESERVAS-API/
├── app/
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── reserva_controller.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── reserva.py
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   └── main.py
├── Dockerfile
└── requirements.txt
```

---

## 🛠 Tecnologias

![Python](https://img.shields.io/badge/Python-0D1117?style=for-the-badge&logo=python&logoColor=yellow&labelColor=0D1117)
![Flask](https://img.shields.io/badge/Flask-0D1117?style=for-the-badge&logo=flask&logoColor=white&labelColor=0D1117)

## 🧰 Ferramentas

![Git](https://img.shields.io/badge/Git-0D1117?style=for-the-badge&logo=Git&logoColor=white&labelColor=0D1117)
![GitHub](https://img.shields.io/badge/-GitHub-0D1117?style=for-the-badge&logo=github&labelColor=0D1117)
![Postman](https://img.shields.io/badge/Postman-0D1117?style=for-the-badge&logo=Postman&logoColor=white&labelColor=0D1117)
![Docker](https://img.shields.io/badge/-Docker-0D1117?style=for-the-badge&logo=docker&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/-Visual%20Studio%20Code-0D1117?style=for-the-badge&logo=visual%20studio%20code&logoColor=white&labelColor=0D1117)
