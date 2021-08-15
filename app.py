from logging import info
from flask import Flask,render_template,url_for,request,redirect
import random
import itertools
import numpy as np
import json

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == "POST" and 'team' in request.form:
        global numero_squadre
        numero_squadre = request.form['team']

        return redirect(url_for("league"))
    else: 
        return render_template("index.html")

@app.route("/league",methods=["GET","POST"])
def league():
    team_n = int(numero_squadre)
    information = request.data.decode('utf-8')
    
    if information != "":
        information = json.loads(information)
        
        set_size = 2
        schedule = set()
        teams = information
        for comb in itertools.product(teams, repeat=set_size):
            comb = sorted(list(comb))
            if len(set(comb)) == set_size:
                schedule.add(tuple(comb))

        schedule = list(schedule)
        
        random.shuffle(schedule)
        schedule = np.asarray(schedule)
        print(schedule)
        print(type(schedule))

    return render_template("league.html",team_n = team_n)

if __name__ == '__main__':
    app.run(debug=True)
    