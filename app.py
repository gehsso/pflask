from flask import Flask, render_template, request,redirect, flash

from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO

app = Flask(__name__)
app.secret_key = "uma_chave_muito_secreta_e_unica"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/sobre')
def sobre_o_sistema():
     return render_template('sobre.html')


@app.route('/ajuda')
def ajuda():
    return render_template('ajuda.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/aluno')
def listar_aluno():
    dao = AlunoDAO()
    lista = dao.listar()
    return render_template('aluno/lista.html',lista=lista)

# Rota para exibir o formulário
@app.route('/aluno/form') # rota formulario de aluno
def form_aluno():
    # rederiza o arquivo formulario com aluno vazio
    return render_template('aluno/form.html',aluno=None) 

@app.route('/aluno/salvar/', methods=['POST'])  # Inserção
def salvar_aluno(id=None):
    nome = request.form['nome']
    idade = request.form['idade']
    cidade = request.form['cidade']
    dao = AlunoDAO()
    result = dao.salvar(id, nome, idade, cidade) 

    if result["status"] == "ok":
        flash("Aluno salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/aluno')



@app.route('/professor')
def listar_professor():
    dao = ProfessorDAO()
    lista = dao.listar()
    return render_template('professor/lista.html',lista=lista)


@app.route('/saudacao1/<nome>')
def saudacao1(nome):
    # gravar no banco nome
    # dao.salvar(nome)
    return render_template('saudacao/saudacao.html',valor_recebido=nome)



@app.route('/saudacao2/')
def saudacao2():
    nome = request.args.get('nome')
    return render_template('saudacao/saudacao.html',valor_recebido=nome)



@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    senha = request.form['senha']
    email = request.form['email']
    dados = f"Usuário: {usuario}, Senha: {senha}, E-mail: {email}"
    return render_template('saudacao/saudacao.html',valor_recebido=dados)





if __name__ == '__main__':
    app.run(debug=True)















"""
lista_alunos = [
        (1, "Ana Beatriz Silva", 20, "Teresina"),
        (2, "Carlos Eduardo Lima", 22, "Parnaíba"),
        (3, "Mariana Souza", 19, "Picos"),
        (4, "Rafael Oliveira", 23, "Floriano"),
        (5, "Juliana Costa", 21, "Campo Maior"),
        (6, "Pedro Henrique", 20, "Oeiras"),
        (7, "Fernanda Gomes", 18, "Piripiri"),
        (8, "Lucas Almeida", 22, "Altos"),
        (9, "Bianca Rocha", 24, "Esperantina"),
        (10, "Matheus Ribeiro", 19, "Barras"),
    ]
    
    
    
    
       <table class="table table-bordered table-striped">
        <thead class="table-dark">
        <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Idade</th>
            <th>Cidade</th>
            <th>Ações</th>
        </tr>
    </thead>
    <tbody>
        {% for item in lista_alunos %}
        <tr>
            <td>{{ item[0] }}</td>
            <td>{{ item[1] }}</td>
            <td>{{ item[2] }}</td>
            <td>{{ item[3] }}</td>
            <td>
              
            </td>
        </tr>
        {% endfor %}
    </tbody>
    </table>
    
    
context = {'msg': 'Teste', 'lista_alunos': alunos}
return render_template('aluno/lista.html', **context)

"""