
from flask import Flask, render_template
#render_template permite colcar as paginas como return dos def, ele ja procura pela por uma pagina chamda 'templates', por isso dá pra por direto o nome sa pagina, sem indicar o endereço inteiro

app = Flask(__name__)
@app.route("/")
def homepaeg():
  return render_template("homepage.html")
@app.route("/contatos")
def contatos():
    return render_template("contatos.html")
@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)
#colocar o site no ar
if __name__ == "__main__":
  app.run(debug=True) #o debug é para nao ter que ficar rodando o tempo inteiro