import data
import random
from flask import Flask, render_template

app = Flask(__name__)


tours_number = []

for i in range(6):
    a = random.randint(1, 16)
    if tours_number.count(a) > 1:
        a = random.randint(1, 16)
    tours_number.append(a)

print (tours_number)

@app.route('/')
def index():
    index_page = render_template("index.html", title=data.title, subtitle=data.subtitle, description=data.description, departures=data.departures, tours=data.tours, tours_number=tours_number)
    return index_page

@app.route('/departure/')
def departure():
    departure_page = render_template("departure.html")
    return departure_page

@app.route('/tour/')
def tour():
    tour_page = render_template("tour.html")
    return tour_page

if __name__ == '__main__':
    app.run()

