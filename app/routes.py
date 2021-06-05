from app import db
from app.models.planet import Planet
from flask import request, Blueprint, make_response

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])

# Create a new Planet
def create_new_planet():
    # In order for this to work
    # The .get_json method needs to passed either:
    # request.data or fore=True
    request_body = request.get_json(request.data)
    new_planet = Planet(
        name=request_body["name"],
        description=request_body["description"],
        size=request_body["size"]
    )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} succesfully created", 201)

# get all planets
def get_all_planets():
    return "get all planets"

# get/ read specific planet.
def get_specific_planet_info():
    return "specific info for planet"
