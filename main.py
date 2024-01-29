from flask import Flask, render_template, request, redirect, send_file
from find_jobs_data import find_jobs_data
from save_to_file import save_to_file
app = Flask("JobScraper")

db={}

@app.route("/") 
def home():
    return render_template('home.html')

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else :
        jobs = find_jobs_data(keyword)
        db[keyword] = jobs
    return render_template("search.html", keyword = keyword, jobs = jobs)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}_jobs.csv", as_attachment=True)
     
app.run("127.0.0.1")