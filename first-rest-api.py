import mysql.connector
from flask import Flask, jsonify
from flask_cors import CORS


#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="CLASH_ROYALE"
)
mycursor = mydb.cursor()

app = Flask(__name__)
CORS(app)




@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/getAllDataInHtml")
def getAllData():
    
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit")
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    rv = mycursor.fetchall()
    json_data=[]

    for result in rv:
        json_data.append(dict(zip(row_headers,result)))

    return jsonify(json_data)

    


@app.route("/air_transport")
def air_transport():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Transport = 'Air'")
    myresult = mycursor.fetchall()
    result = [];

    for x in myresult:
        print(x);
        result.append(x);
    return result


@app.route("/epic_unit")
def epic_unit():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Rarity = 'Epic'")
    myresult = mycursor.fetchall()
    result = [];

    for x in myresult:
        print(x);
        result.append(x);
    return result


@app.route("/speed")
def speed():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Speed = 'Fast (90)'")
    myresult = mycursor.fetchall()
    result = [];

    for x in myresult:
        print(x);
        result.append(x);
    return result



@app.route("/hit_speed")
def hit_speed():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Hit_Speed = '1.2 sec'")
    myresult = mycursor.fetchall()
    result = [];

    for x in myresult:
        print(x);
        result.append(x);
    return result




if __name__ == '__main__':
   app.run(debug=True)