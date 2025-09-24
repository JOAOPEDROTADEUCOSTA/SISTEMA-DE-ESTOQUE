from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)

database.init_db()

@app.route("/")
def index():
    produtos = database.get_all_produtos()
    return render_template("index.html", produtos=produtos)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    tipo = request.form["tipo"]
    nome = request.form["nome"]
    quantidade = int(request.form["quantidade"])
    preco = float(request.form["preco"])

    database.add_produto(tipo, nome, quantidade, preco)
    return redirect(url_for("index"))

@app.route("/remover/<int:id>")
def remover(id):
    database.remove_produto(id)
    return redirect(url_for("index"))

@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    if request.method == "POST":
        tipo = request.form["tipo"]
        nome = request.form["nome"]
        quantidade = int(request.form["quantidade"])
        preco = float(request.form["preco"])
        database.update_produto(id, tipo, nome, quantidade, preco)
        return redirect(url_for("index"))

    produto = database.get_produto(id)
    produtos = database.get_all_produtos()
    return render_template("index.html", produtos=produtos, produto_edit=produto)

    produto = database.get_produto(id)
    return render_template("editar.html", produto=produto)

if __name__ == "__main__":
    app.run(debug=True)
