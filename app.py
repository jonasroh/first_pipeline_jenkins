from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá mundo!'

@app.route('/hello')
def hello():
    return 'Olá, visitante!'

@app.route('/name', methods=['GET', 'POST'])
def name():
    if request.method == 'POST':
        name = request.form['name']
        return f'Olá, {name}!'
    return '''
        <form method="POST">
            <label for="name">Digite seu nome:</label>
            <input type="text" id="name" name="name">
            <input type="submit" value="Enviar">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
