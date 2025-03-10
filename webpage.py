from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/status')
def status():
    return render_template('status.html')

@app.route('/scaling')
def scaling():
    return render_template('scaling.html')

@app.route('/project-outline')
def projectoutline():
    return render_template('project-outline.html')

if __name__ == '__main__':
    app.run(debug=True)
