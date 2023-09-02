from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    title='my flask project'
    button_label='Click Me'
    return render_template('index.html',title=title,button_label=button_label)

if __name__=='main':
    app.run(debug=True)
