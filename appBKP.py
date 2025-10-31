from flask import Flask, render_template


app = Flask(__name__)


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
                (1, "Ana Beatriz Silva", 20, "Teresina"),
        (2, "Carlos Eduardo Lima", 22, "Parnaíba"),
        (3, "Mariana Souza", 19, "Picos"),
        (4, "Rafael Oliveira", 23, "Floriano"),
        (5, "Juliana Costa", 21, "Campo Maior"),
        (6, "Pedro Henrique", 20, "Oeiras"),
        
    ]
    
    return render_template('aluno/lista.html',lista_alunos=lista_alunos)





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