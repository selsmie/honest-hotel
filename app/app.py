from flask import Flask, render_template

from controllers.guests_controller import guests_blueprint
from controllers.rooms_controller import rooms_blueprint
from controllers.reservations_controller import reservations_blueprint
import repositories.reservation_repository as reservation_repository
import repositories.room_repository as room_repository

app = Flask(__name__)

app.register_blueprint(guests_blueprint)
app.register_blueprint(rooms_blueprint)
app.register_blueprint(reservations_blueprint)


@app.route('/')
def main():
    arrivals = reservation_repository.total_arrivals()
    departures = reservation_repository.total_departures()
    expected_occupancy = reservation_repository.expected_occupancy()
    current_occupancy = reservation_repository.current_occupancy()
    reservation_repository.arrival_staus()
    return render_template('index.html', arrivals=arrivals, departures=departures, expected_occupancy=expected_occupancy, current_occupancy=current_occupancy)

if __name__ == '__main__':
    app.run()