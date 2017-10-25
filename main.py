from flask import Flask, jsonify, request
from modelo import criar_tarefa, listar_tarefas

app = Flask('Meu app')


@app.route('/task', methods=['POST'])
def criar():
    # recebe o título e a descrição através do corpo da requisição
    titulo = request.form['titulo']
    descricao = request.form['descricao']
    # utiliza estes valores para criar uma tarefa
    # a função criar tarefa foi desenvolvida e testada no passo anterior
    tarefa = criar_tarefa(titulo, descricao)
    # retorna o resultado em um formato json
    return jsonify({
        'id': tarefa.id,
        'titulo': tarefa.titulo,
        'descricao': tarefa.descricao,
        'status': tarefa.status,
    }), 201

@app.route('/task', methods=['GET'])
def listar():
    tarefas = []
    for tarefa in listar_tarefas():
        tarefas.append({
            'id': tarefa.id,
            'titulo': tarefa.titulo,
            'status': tarefa.status,
        })
    return jsonify(tarefas) 
