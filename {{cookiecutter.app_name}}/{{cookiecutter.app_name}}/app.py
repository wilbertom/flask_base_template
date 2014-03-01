"""
{{cookiecutter.app_name}}

Base server for {{cookiecutter.app_name}}
author: {{cookiecutter.author}}
email: {{cookiecutter.email}}

"""

from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

