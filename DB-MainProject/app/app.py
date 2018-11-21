from flask import Flask
import json
import requests

app = Flask(__name__)

DATA = {"Departament":
			{"name": "DevOps"},
		"Team": [{"depart_id": 1,
			"name": "Avengers",
                        "team_id": 1,
			"manager_id": 1}],
		"Employee": [{"team_id": 1,
			"name": "Name",
			"sname": "Surname",
			"exp": 1,
			"position": "Designer",
			"salary": 500,
                        "coefficient": 1.5},
                       {"team_id": 1,
                        "name": "Max",
                        "sname": "Surname",
                        "exp": 1,
                        "position": "Designer",
                        "salary": 500,
                        "coefficient": 0.5}]}
DEP = {
         "Department": 
                   [{"name": "Ben"}] 
      }
Teams = {
          "Team": [{
                    "depart_id": 1,
                    "name": "Team1",
                    "manager_id": 5,
                    "team_id": 1
                  }]
         }

Employees = {
           "Employee": [{
                      "team_id": 1,
                      "name": "Oleh",
                      "sname": "Olehhh",
                      "exp": 3,
                      "position": "Manager",
                      "salary": 1500,
                      "coefficient": 1
                       },
                        {"team_id": 1,
                        "name": "Name",
                        "sname": "Surname",
                        "exp": 3,
                        "position": "Developer",
                        "salary": 500,
                        "coefficient": 1.5},
                       {"team_id": 1,
                        "name": "Max",
                        "sname": "Surname",
                        "exp": 6,
                        "position": "Developer",
                        "salary": 500,
                        "coefficient": 0.5}]
             }




@app.route('/get-info', methods=['GET'])
def reply_info():
    return json.dumps(DATA)

@app.route('/get-team', methods=['GET'])
def reply_team():
    return json.dumps(Teams)

@app.route('/get-empl', methods=['GET'])
def reply_empl():
    return json.dumps(Employees)

@app.route('/get-dep', methods=['GET'])
def reply_dep():
    return json.dumps(DEP)


if __name__=='__main__':
    app.run(debug=True)
