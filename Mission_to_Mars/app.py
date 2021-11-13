from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_stuff")


@app.route("/")
def index():
    mars_listings = mongo.db.mars_listings.find_one()
    return render_template("index.html", mars_listings=mars_listings)


@app.route("/scrape")
def scraper():
    mars_listings = mongo.db.mars_listings
    mars_listings_data = scrape_mars.scrape()
    mars_listings.update({}, mars_listings_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
