from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_inicio():
    resposta = client.get("/")
    assert resposta.status_code == 200
    assert resposta.json() == {"mensagem": "Bem-vindo ao meu primeiro API com FastAPI!"}


def test_sobre():
    resposta = client.get("/sobre")
    assert resposta.status_code == 200
    dados = resposta.json()
    assert dados["nome"] == "Yuri Franca"
    assert dados["profissao"] == "Python Developer"
    assert "Python" in dados["skills"]


def test_projetos():
    resposta = client.get("/projetos")
    assert resposta.status_code == 200
    dados = resposta.json()
    assert "projetos" in dados
    assert len(dados["projetos"]) == 4


def test_criar_tarefa():
    resposta = client.post("/tarefas", json={
        "titulo": "Estudar FastAPI",
        "descricao": "Aprender rotas GET e POST",
        "prazo": "Hoje 23h"
    })
    assert resposta.status_code == 200
    dados = resposta.json()
    assert dados["mensagem"] == "Tarefa criada com sucesso!"
    assert dados["tarefa"]["titulo"] == "Estudar FastAPI"


def test_atualizar_tarefa():
    resposta = client.put("/tarefas/1", json={
        "titulo": "Estudar FastAPI avancado",
        "descricao": "Aprender PUT e DELETE",
        "prazo": "Amanha"
    })
    assert resposta.status_code == 200
    assert "atualizada" in resposta.json()["mensagem"]


def test_apagar_tarefa():
    resposta = client.delete("/tarefas/1")
    assert resposta.status_code == 200
    assert "deletada" in resposta.json()["mensagem"]