# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    selected_project = None
    if request.method == 'POST':
        if 'button_python' in request.form:
            selected_project = 'python'
        elif 'button_discord' in request.form:
            selected_project = 'discord'
        elif 'button_html' in request.form:
            selected_project = 'html'
        elif 'button_db' in request.form:
            selected_project = 'db'
    return render_template('index.html', selected_project=selected_project)

@app.route('/feedback', methods=['POST'])
def feedback():
    email = request.form.get('email')
    comment = request.form.get('text')
    with open('feedback.txt', 'a', encoding='utf-8') as f:
        f.write(f'{email}: {comment}\n')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
