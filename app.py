#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Hero, Hero_Power, Power

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)
api =Api(app)

@app.route('/')
def home():
    return ''

@app.route('/heroes')
def get_heroes(): #gets all heroes
    heroes =[]

    for hero in Hero.query.all():
        hero ={
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name
        }
        heroes.append(hero)
        response = make_response(jsonify(heroes),200)
    return response

@app.route('/heroes/<int:id>', methods =['GET'])
def get_hero_byID(id):
    hero = Hero.query.filter_by(id=id).first()

    if hero == None:
        response = make_response(
                jsonify({
                    "error": "hero not found"
                    }),
                404
        )
        return response   
    else:

        hero_dict =hero.to_dict()

        response = make_response(
            jsonify(hero_dict),
            200
        )
        response.headers["Content-Type"] = "application/json"

        return response
    
@app.route('/powers')
def get_powers():
    powers =[]

    for power in Power.query.all():
        power ={
            "id": power.id,
            "name": power.name,
            "description": power.description
        }
        powers.append(power)
        response = make_response(jsonify(powers),200)
    return response

@app.route('/powers/<int:id>', methods =['GET'])
def get_power_byID(id):
    power = Power.query.filter_by(id=id).first()

    if power == None:
        response = make_response(
                jsonify({
                    "error": "power not found"
                    }),
                404
        )
        return response   
    else:

        power_dict =power.to_dict()

        response = make_response(
            jsonify(power_dict),
            200
        )
        response.headers["Content-Type"] = "application/json"

        return response
    
class HeroPower(Resource): #handle post using flask restful
   def post(self):

    new_hero_power = Hero_Power(
        strength=request.form['strength'],
        power_id=request.form['power_id'],
        hero_id=request.form['hero_id']
    )

    db.session.add(new_hero_power)
    db.session.commit()

    response_dict = new_hero_power.to_dict()

    response = make_response(
        jsonify(response_dict),
        201,
    )

    return response

api.add_resource(HeroPower, '/hero_powers')
 




if __name__ == '__main__':
    app.run(port=5555)
