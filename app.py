import data
import random
from flask import Flask, render_template

app = Flask(__name__)


tours_number = []

while len(tours_number) != 6:
    a = random.randint(1, 16)
    if a in tours_number:
        a = random.randint(1, 16)
    else:
        tours_number.append(a)
    print(tours_number.count(a))

print (tours_number)

@app.route('/')
def index():
    index_page = render_template("index.html", title=data.title, subtitle=data.subtitle, description=data.description, departures=data.departures, tours=data.tours, tours_number=tours_number)
    return index_page

@app.route('/departure/')
def departure():
    departure_page = render_template("departure.html")
    return departure_page

@app.route('/tour/<int:uid>')
def tour(uid):
    depar = data.departures[data.tours[uid]['departure']]
    tour_page = render_template("tour.html", departures=data.departures, tours=data.tours, tours_number=[1], uid=uid, depar=depar)
    return tour_page

@app.errorhandler(404)
def not_found(e):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!"

if __name__ == '__main__':
    app.run()

