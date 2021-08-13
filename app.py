from flask import Flask,render_template,url_for,request
from werkzeug.utils import redirect


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == "POST" and 'team' in request.form:
        global numero_squadre
        numero_squadre = request.form['team']

        return redirect(url_for("league"))
    else: 
        return render_template("index.html")

@app.route("/league")
def league():
    team_n = int(numero_squadre)
    return render_template("league.html",team_n = team_n)

if __name__ == '__main__':
    app.run(debug=True)
    