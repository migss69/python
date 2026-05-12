from flask import Flask


app = Flask(__name__) 

@app.route('/') 
def ola_mundo():
    return '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bem-vindo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f8ff;
            color: #333;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #4CAF50;
            color: white;
            padding: 1rem;
            text-align: center;
        }
        main {
            padding: 2rem;
            text-align: center;
        }
        footer {
            background-color: #4CAF50;
            color: white;
            padding: 1rem;
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
        }
    </style>
</head>
<body>
    <header>
        <h1>Bem-vindo ao Meu Site</h1>
    </header>
    <main>
        <p>Este é um exemplo de página HTML bonita usando Flask.</p>
        <p>Divirta-se criando suas aplicações!</p>
    </main>
    <footer>
        <p>&copy; 2023 Meu Site</p>
    </footer>
</body>
</html>x''' 

@app.route('/hello') 
def hello():
    return 'Hello, World!' 

if __name__ == '__main__':
    app.run(debug=True) 
