# 📚 API de Atividades

Este repositório contém a **API de Atividades**, desenvolvida com **Flask** e **SQLAlchemy**, como parte de uma arquitetura baseada em **microsserviços**.

## 🧩 Arquitetura

A API de Reserva de Atividades é um **microsserviço** que faz parte de um sistema maior de [School System](https://github.com/LarissaPiresDev/API---School-System)
, sendo responsável exclusivamente pelo gerenciamento das atividades de salas por turma.


⚠️ **Esta API depende de outra API de Gerenciamento Escolar (School System)**, que deve estar em execução e exposta localmente. A comunicação entre os serviços ocorre via **requisições HTTP REST**, para validar:

- Se o **Professor** existe (`GET /professores/<id>`)

## 🚀 Tecnologias Utilizadas

- Python
- Flask
- SQLite (como banco de dados local)
- Requests (para consumo da API externa)


---

## ▶️ Como Executar a API

### 1. Clone o repositório

```bash
git clone https://github.com/LarissaPiresDev/Atividade.git
cd Atividade
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a API

```bash
python .\ApiAtv\app.py
```

A aplicação estará disponível em:
📍 `http://127.0.0.1:5004`

📝 **Observação:** O banco de dados é criado automaticamente na primeira execução.

---

## 📡 Endpoints Principais

- `GET /atividades` – Lista todas as atividades
- `POST /atividades` – Cria uma nova atividade
- `GET /atividades/<id>` – Detalha uma atividade

### Exemplo de corpo JSON para criação:

```json
    {
        "professor_id": 1,
        "enunciado": "Quanto é 1 + 1?",
        "alternativas": "["A-) 2", "B-) 3", "C-) 4"" D-) 5", "E-)6"]",
        "resposta": "A"
    }
```
## 🔗 Dependência Externa

Certifique-se de que a **API de Gerenciamento Escolar** esteja rodando em:

```
http://127.0.0.1:5003
```

---

## 📦 Estrutura do Projeto

```
reserva-salas/
│
├── 📁 ApiAtv/
│   ├── 📁 instance/
│   │   └── 🛢️ atividade.db
│   ├── 📁 atividadesmicrosservicos/
│   │   ├── 🐍 atividade_model.py
│   │   └── 🐍 atividade_routes.py
│   ├── 🐍 app.py
│   └── 🐍 config.py
│
├── 🐳 Dockerfile
├── 📄 requirements.txt
└── 📄 README.md
```
