from flask import Flask, request, render_template_string

app = Flask(__name__)

def show_the_login_form():
    return render_template_string("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Login</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background: linear-gradient(90deg, #00274d, #0047ab);
                    color: white;
                    text-align: center;
                }
                h1 {
                    font-size: 2.5rem;
                    margin-top: 20px;
                }
                form {
                    background: rgba(255, 255, 255, 0.1);
                    padding: 20px;
                    border-radius: 10px;
                    display: inline-block;
                    margin-top: 50px;
                }
                input[type="text"], input[type="password"] {
                    padding: 10px;
                    margin: 10px 0;
                    border: none;
                    border-radius: 5px;
                    width: 80%;
                }
                input[type="submit"] {
                    background: #ff0000;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 5px;
                    cursor: pointer;
                    font-size: 1rem;
                }
                input[type="submit"]:hover {
                    background: #cc0000;
                }
                footer {
                    margin-top: 50px;
                    font-size: 0.8rem;
                    color: #ccc;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to the Red Bull Inspired Login</h1>
            <form method="POST">
                <input type="text" name="usuario" placeholder="Username" required>
                <input type="password" name="senha" placeholder="Password" required>
                <input type="submit" value="Login">
            </form>
            <footer>
                <p>Powered by Flask | Inspired by Red Bull Racing</p>
            </footer>
        </body>
        </html>
    """)

def do_the_login():
    usuario_digitado = request.form.get('usuario')
    senha_digitado = request.form.get('senha')
    
    usuarios = [
        {"usuario":"miguel","senha": "22301259"},
        {"usuario":"janaina","senha": "cotemig2026"},
        {"usuario":"antonio","senha": "cotemig2026"},
        {"usuario":"dolga","senha": "cotemig2026"}
    ]
    for usuario in usuarios:
        if (
            usuario["usuario"] == usuario_digitado and
            usuario["senha"] == senha_digitado

        ):
            return f"<h1> Bem-Vindo, {usuario_digitado}! </h1>"

    return f"<h1> Login Inválido </h1>"


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == "__main__":
    app.run(debug=True)

# site de consulta https://flask.palletsprojects.com/en/stable/quickstart/#html-escaping
