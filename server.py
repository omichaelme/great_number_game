from flask import Flask, make_response, request, session, redirect, render_template
from random import randint

app = Flask(__name__)
app.secret_key='ThisIsSecret'

@app.route("/")
def homePage():
    randint(0,101)
    if 'randNum' not in session:
        session['randNum'] = int(randint(0,101))
    print(session['randNum'])
    TooLow = False
    TooHigh = False
    GoodNum = False
    ErrorMsg = False
    if 'inputNum' not in session:
        pass
    elif session['randNum'] > session['inputNum']:
        TooLow = True
        print(TooLow, "This is too low")
    elif session['randNum'] < session['inputNum']:
        TooHigh = True
        print(TooHigh, " This is too high")
    elif session['randNum'] == session['inputNum']:
        GoodNum = True
        print(GoodNum, " This is the Number!")
    else:
        ErrorMsg = True
    return render_template('randGame.html', TooLow = TooLow, TooHigh = TooHigh, GoodNum = GoodNum, ErrorMsg = ErrorMsg)

@app.route("/user", methods=['POST'])
def create_user():
    print("Got Post Info")
    inputNum = int(request.form['inputNum'])
    session['inputNum'] = inputNum
    print(session['inputNum'])
    return redirect('/')

@app.route("/restart")
def clear_session():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)
    