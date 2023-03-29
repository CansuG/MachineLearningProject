from flask import Flask
from app import views

from flask import render_template, request, jsonify
import matplotlib.image as matimg

from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline, AutoModelForSeq2SeqLM


app = Flask(__name__) # webserver gateway interphase (WSGI)

app.add_url_rule(rule='/',endpoint='home',view_func=views.index)
app.add_url_rule(rule='/app/',endpoint='app',view_func=views.app)
app.add_url_rule(rule='/app/gender/',
                 endpoint='gender',
                 view_func=views.genderapp,
                 methods=['GET','POST'])
app.add_url_rule(rule='/app/transformer/', endpoint='transformer',view_func=views.use_transformer, methods=['GET','POST'])


if __name__ == "__main__":
    app.run(debug=True)