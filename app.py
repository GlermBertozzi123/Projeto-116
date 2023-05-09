# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "Guilherme" # escreva seu nome
    idade = "13 anos" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route("/pai")
def father():

    nome = "Demian" # escreva seu nome
    idade = "Acho que 47 anos" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)


# defina a rota para a página da mãe
@app.route("/mãe")
def mother():

    nome = "Cleise" # escreva seu nome
    idade = "Não vou dizer a idade kkkk" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)


# defina a rota para a página do amigo
@app.route("/amigo")
def friend():

    nome = "Bernardo" # escreva seu nome
    idade = "12 anos" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)


# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
