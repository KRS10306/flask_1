from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
{
'id' : 1,
'title' : "Data Anaylist",
'location' : "Delhi,India",
'salary' : "Rs. 1,000,000"
},
{
'id' : 2,
'title' : "Data Scientist",
'location' : "Bengluru,India",
'salary' : "Rs. 2,000,00"
},
{
'id' : 3,
'title' : 'Front-end Enginner',
'location' : 'remote',
'salary' : 'Rs. 100,000'
},
{
'id' : 4,
'title' : 'Back-end Enginner',
'location' : 'Mosscow,Russia'
}
]

@app.route("/")  # ("/") ->means path where we want the thing written below
def hello_world():
    return render_template('index.html',jobs = JOBS, company_name = 'Krish') # connects html to our JOBS database

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug =True)
