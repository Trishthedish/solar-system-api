from app import db
from app.models.planet import Planet
from flask import request, Blueprint, make_response, jsonify

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST","GET"])
def handle_planets():
    if request.method == "POST":
        request_body = request.get_json(request.data)
        new_planet = Planet(
            name=request_body["name"],
            description=request_body["description"],
            size=request_body["size"]
        )
        db.session.add(new_planet)
        db.session.commit()
        return make_response(f"Planet {new_planet.name} succesfully created", 201)

    elif request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "size": planet.size
            })
        return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_planet(planet_id):
    planet = Planet.query.get(planet_id)

    if request.method == "GET":
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "size": planet.size
        }

    elif request.method == "PUT":
        form_data = request.get_json()
        planet.name = form_data["name"]
        planet.description = form_data["description"]
        planet.size = form_data["size"]
        db.session.commit()
        return make_response(f"Planet #{planet.id} has been updated.", 201)

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return make_response(f"Planet #{planet.id} sucessfully deleted.")