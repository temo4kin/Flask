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
    #print(tours_number.count(a))

#print (tours_number)

@app.route('/')
def index():
    index_page = render_template("index.html", title=data.title, subtitle=data.subtitle, description=data.description, departures=data.departures, tours=data.tours, tours_number=tours_number)
    return index_page

@app.route('/departure/<uin>')
def departure(uin):
    tour_dep_keys = []
    tour_dep_values = []
    tour_dep_nights = []
    tour_dep_price = []
    i = 1
    for tour in data.tours:
        if data.tours[tour]['departure'] == uin:
            tour_dep_values.append(data.tours[tour])
            tour_dep_keys.append(i)
            i += 1
    for k in range(len(tour_dep_values)):
        tour_dep_price.append(tour_dep_values[k].get('price'))

    for k in range(len(tour_dep_values)):
        tour_dep_nights.append(tour_dep_values[k].get('nights'))

    sum_tour_dep = len(tour_dep_values)
    number_sum_tour_dep = int(str(sum_tour_dep)[-1])
    print(number_sum_tour_dep)
    # tour_departure = dict(zip(tour_dep_keys, tour_dep_values))
    departure_page = render_template("departure.html", tour_dep_values=tour_dep_values, sum_tour_dep=sum_tour_dep, departures=data.departures, uin=uin, number_sum_tour_dep=number_sum_tour_dep, tour_dep_nights=tour_dep_nights, tour_dep_price=tour_dep_price)
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

