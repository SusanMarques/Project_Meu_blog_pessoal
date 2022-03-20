from app import app

@app.route('/')
@app.route('/index')
def index():
    return '''
    <html>
        <head><tittle>Susan Karin</title></head>
        <body>
            <h1>Bem vindo ao meu blog pessoal!</h1>
        </body>
    </html>


    '''