from flask import render_template
from flask import request
from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

@app.route('/')
def index():
    user = {'username': 'Paul'}
    return render_template('index.html', title='Home', user=user)

@app.route('/hello')
def hello():
    return 'Hello, World'

# @app.route('/<name>')
# def hello_name(name):
#     return "Hello {}!".format(name)


@app.route('/cars', methods=['POST', 'GET'])
def handle_cars():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_car = CarsModel(name=data['name'], model=data['model'], doors=data['doors'])
            db.session.add(new_car)
            db.session.commit()
            return {"message": f"car {new_car.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        cars = CarsModel.query.all()
        results = [
            {
                "name": car.name,
                "model": car.model,
                "doors": car.doors
            } for car in cars]

        return {"count": len(results), "cars": results}

# if __name__ == '__main__':
#     app.run()