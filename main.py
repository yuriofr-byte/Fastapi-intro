from fastapi import FastAPI
from pydantic import BaseModel

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


class Tarefa(BaseModel):
    titulo: str
    descricao: str
    prazo: str


@app.post("/tarefas")
def criar_tarefa(tarefa: Tarefa):
    return {
        "mensagem": "Tarefa criada com sucesso!",
        "tarefa": tarefa
    }

@app.put("/tarefas/{id}")
def atualizar_tarefa(id: int, tarefa: Tarefa):
    return {
        "mensagem": "Tarefa atualizada com sucesso!",
        "tarefa": tarefa
    }

@app.delete("/tarefas/{id}")
def deletar_tarefa(id: int):
    return {
        "mensagem": f"Tarefa com id {id} deletada com sucesso!"
    }   