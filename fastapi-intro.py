from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def inicio():
    return {"mensagem": "Bem-vindo ao meu primeiro API com FastAPI!"}


@app.get("/sobre")
def sobre():
    return {
        "nome": "Yuri Franca",
        "profissao": "Python Developer",
        "skills": ["Python", "FastAPI", "IA", "Automacao"]
    }


@app.get("/projetos")
def projetos():
    return {
        "projetos": [
            {"nome": "Bot de Cambio", "github": "github.com/yuriofr-byte/bot-precos"},
            {"nome": "Dashboard com IA", "github": "github.com/yuriofr-byte/Dashboard-ia"},
            {"nome": "Analisador de Curriculos", "github": "github.com/yuriofr-byte/analisador-curriculo"},
            {"nome": "TaskMind", "github": "github.com/yuriofr-byte/TaskMind"}
        ]
    }