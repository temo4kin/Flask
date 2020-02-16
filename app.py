import random
from flask import Flask, render_template, abort
from data import *

app = Flask(__name__)


tours_number = []

while len(tours_number) != 6:
    a = random.randint(1, 16)
    if a in tours_number:
        a = random.randint(1, 16)
    else:
        tours_number.append(a)
    #print(tours_number.count(a))

#print (tours_number)

@app.route('/')
def index():
    index_page = render_template("index.html", title=title, subtitle=subtitle, description=description, departures=departures, tours=tours, tours_number=tours_number)
    return index_page

@app.route('/departure/<uin>')
def departure(uin):
    tour_dep_keys = []
    dep_values = []
    dep_nights = []
    dep_price = []
    i = 1

    for tour in tours:
        if tours[tour]['departure'] == uin:
            dep_values.append(tours[tour])
            tour_dep_keys.append(i)
            i += 1
            print(tours[tour]['departure'])
    for k in range(len(dep_values)):
        dep_price.append(dep_values[k].get('price'))

    for k in range(len(dep_values)):
        dep_nights.append(dep_values[k].get('nights'))

    sum_dep = len(dep_values)
    sum_tour = int(str(sum_dep)[-1])

    departure_page = render_template("departure.html", dep_values=dep_values, sum_dep=sum_dep, uin=uin, sum_tour=sum_tour, dep_nights=dep_nights, dep_price=dep_price, departures=departures)
    return departure_page


@app.route('/tour/<int:uid>')
def tour(uid):
    try:
        depar = departures[tours[uid]['departure']]
    except KeyError as err:
        abort(404)
    tour_page = render_template("tour.html", departures=departures, tours=tours, tours_number=[1], uid=uid, depar=depar)
    return tour_page


@app.errorhandler(404)
def not_found(e):
    output = render_template("404.html", title=title, subtitle=subtitle, departures=departures, description='Страница не найдена! Вернитесь на главную.')
    return output

if __name__ == '__main__':
    app.run()

