from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from gradecalc import gradecalc
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('secret_key')

class studentInfo(FlaskForm):
    s_name = StringField('Name: ')
    s_h = IntegerField('Homework score: ')
    s_a = IntegerField('Assessment score: ')
    s_e = IntegerField('Exam score: ')
    submit = SubmitField('Calculate grade')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = studentInfo()
    if request.method == 'POST':
        name = form.s_name.data
        h = form.s_h.data
        a = form.s_a.data
        e = form.s_e.data
        message = gradecalc(name, h, a, e)
        return render_template('home.html', form=form, message=message)
    return render_template('home.html', form=form, message=None)

if __name__ == '__main__':
    app.run(debug = True)