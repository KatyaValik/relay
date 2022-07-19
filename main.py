from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'well-secret-password'


class MyForm(FlaskForm):
    on1 = SubmitField(label='Turn on relay 1')
    on2 = SubmitField(label='Turn on relay 2')
    off1 = SubmitField(label='Turn off relay 1')
    off2 = SubmitField(label='Turn off relay 1')
    off = SubmitField(label='Turn off relay 1 and relay 2')
    on1_sec = SubmitField(label='Turn on relay 1 for one second')
    on2_sec = SubmitField(label='Turn on relay 2 for one second')


status1 = 'Relay 1 turned off'
status2 = 'Relay 2 turned off'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()

    if form.validate_on_submit():
        global status1
        global status2
        if form.on1.data:
            status1 = 'Relay 1 turned on'
        elif form.off1.data:
            status1 = 'Relay 1 turned off'
        if form.on2.data:
            status2 = 'Relay 2 turned on'
        elif form.off2.data:
            status2 = 'Relay 2 turned off'
        return render_template('index.html', form=form, status1=status1, status2=status2)

    return render_template('index.html', form=form, status1=status1, status2=status2)


if __name__ == '__main__':
    app.run(debug=True)
