from flask import Flask, render_template, request
from extractors.indeed import scrape_page
from extractors.wwr import scrape_wwr
from extractors.web3 import scrape_web3

app = Flask("JobScrapper")

db = {}

@app.route("/")
def home():

    return render_template("home.html")


@app.route("/search/<keyword>")
def search(keyword):

    if keyword in db:
        jobs = db[keyword]
    else:
        indeed = scrape_page(keyword)
        wwr = scrape_wwr(keyword)
        web3 = scrape_web3(keyword)
        jobs = indeed + wwr + web3
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)


if __name__ == "__main__":
    app.run("0.0.0.0")