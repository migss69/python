from flask import Flask


app = Flask(__name__) 

@app.route('/') 
def ola_mundo():
    return '''<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Currículo Profissional - [Seu Nome]</title>
</head>
<body style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; max-width: 900px; margin: 0 auto; padding: 40px; background-color: #f4f4f4;">

    <!-- HEADER PRINCIPAL -->
    <header style="background-color: #2c3e50; color: white; padding: 30px; border-radius: 8px 8px 0 0; display: flex; justify-content: space-between; align-items: center;">
        <div>
            <h1 style="margin: 0; font-size: 2.5em; text-transform: uppercase; letter-spacing: 2px;">Miguel Anthony</h1>
            <p style="margin: 5px 0 0; font-size: 1.2em; color: #3498db; font-weight: bold;">Desenvolvedor Full Stack Sênior / Especialista em TI</p>
        </div>
        <div style="text-align: right; font-size: 0.9em;">
            <p style="margin: 2px 0;">📍 Belo Horizonte, Brasil</p>
            <p style="margin: 2px 0;">📧 <a href="mailto:seuemail@gmail.com" style="color: #3498db; text-decoration: none;">anthony.m.oliveira02@gmail.com</a></p>
            <p style="margin: 2px 0;">💻 <a href="#" style="color: #3498db; text-decoration: none;">https://github.com/migss69</a></p>
        </div>
    </header>

    <main style="background-color: white; padding: 30px; border-radius: 0 0 8px 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        
        <!-- RESUMO PROFISSIONAL -->
        <section>
            <h2 style="border-bottom: 2px solid #2c3e50; padding-bottom: 5px; color: #2c3e50;">🚀 Resumo Profissional</h2>
            <p>Profissional com mais de <b>3 anos de experiência</b> no desenvolvimento de soluções escaláveis. Especialista em arquitetura de sistemas, com foco em performance e experiência do usuário. Sólido histórico em liderança técnica e entrega de projetos críticos sob alta pressão. Apaixonado por código limpo e automação.</p>
        </section>

        <!-- COMPETÊNCIAS TÉCNICAS (GRID SIMULADA) -->
        <section>
            <h2 style="border-bottom: 2px solid #2c3e50; padding-bottom: 5px; color: #2c3e50;">🛠️ Hard Skills</h2>
            <table style="width: 100%; border-collapse: collapse;">
                <tr>
                    <td style="width: 33%; vertical-align: top; padding: 10px;">
                        <strong>Linguagens:</strong><br>
                        HTML5, CSS3, JavaScript (ES6+), TypeScript, Node.js, Python.
                    </td>
                    <td style="width: 33%; vertical-align: top; padding: 10px;">
                        <strong>Frameworks/Libs:</strong><br>
                        React.js, Next.js, Express, Vue.js, Tailwind CSS.
                    </td>
                    <td style="width: 33%; vertical-align: top; padding: 10px;">
                        <strong>Infra/DB:</strong><br>
                        AWS, Docker, PostgreSQL, MongoDB, CI/CD, Git.
                    </td>
                </tr>
            </table>
        </section>
        
        </section>

        <!-- FORMAÇÃO ACADÊMICA -->
        <section>
            <h2 style="border-bottom: 2px solid #2c3e50; padding-bottom: 5px; color: #2c3e50;">🎓 Formação</h2>
            <p><strong>Colégio Cotemig</strong> - Floresta, Belo Horizonte | <i>2024 – 2026</i></p>
        </section>

        <!-- IDIOMAS E EXTRAS -->
        <section>
            <h2 style="border-bottom: 2px solid #2c3e50; padding-bottom: 5px; color: #2c3e50;">🌎 Idiomas & Certificações</h2>
            <p>
                <b>Inglês:</b> Avançado (C1 - Fluente) | 
                <b>Espanhol:</b> Intermediário | <br>
                <b>12ª Maratona CiberEducação Cisco Brasil - Colégio e Faculdade COTEMIG:</b> Emitido em 2026
            
            </p>
        </section>

    </main>

    <footer style="text-align: center; margin-top: 20px; font-size: 0.8em; color: #7f8c8d;">
        <p>Gerado via código puro em HTML/CSS para demonstrar habilidades estruturais.</p>
    </footer>

</body>
</html>
'''

@app.route('/hello') 
def hello():
    return 'Hello, World!' 

if __name__ == '__main__':
    app.run(debug=True)
