import json
from main import app
from modelo import memdb
from modelo import Tarefa


def test_criar_tarefa():
    with app.test_client() as c:
        # realiza a requisição utilizando o verbo POST
        resp = c.post('/task', data={'titulo': 'titulo',
                                     'descricao': 'descricao'})
        # é realizada a análise e transformação para objeto python da resposta
        data = json.loads(resp.data.decode('utf-8'))
        # 201 CREATED é o status correto aqui
        assert resp.status_code == 201
        assert data['titulo'] == 'titulo'
        assert data['descricao'] == 'descricao'
        # qaundo a comparação é com True, False ou None, utiliza-se o "is"
        assert data['status'] is False

def test_erro_ao_criar_tarefa():
    memdb.clear()
    with app.test_client() as c:
        resp = c.post('/task', data={'titulo': 'titulo'})
        assert resp.status_code == 400

def test_listar_tarefa_sem_conteudo():
    memdb.clear()
    with app.test_client() as c:
        resp = c.get('/task')
        data = json.loads(resp.data.decode('utf-8'))
        assert resp.status_code == 200
        assert data == []


def test_listar_tarefa_com_conteudo():
    memdb.clear()
    tarefa1 = Tarefa('titulo 1', 'descrição')
    memdb[tarefa1.id] = tarefa1
    with app.test_client() as c:
        resp = c.get('/task')
        data = json.loads(resp.data.decode('utf-8'))
        assert resp.status_code == 200
        assert len(data) == 1
        assert 'descricao' not in data[0]


