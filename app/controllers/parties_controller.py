from flask import Blueprint, jsonify, request
from app.services.parties_service import PartiesService


def create_controller(db_path):
    controller = Blueprint("parties", __name__)

    service = PartiesService(db_path)

    @controller.route("/api/v1/parties", methods=["GET"])
    def get_parties():
        limit = request.args.get("limit", default=20, type=int)
        offset = request.args.get("offset", default=0, type=int)

        parties, total = service.get_parties(limit, offset)
        data = [
            {
                "id": partie["id"],
                "serveur_id": partie["serveur_id"],
                "file_id": partie["file_id"],
                "debut": partie["debut"],
                "attente_secondes": partie["attente_secondes"],
                "duree_minutes": partie["duree_minutes"]
            }
            for partie in parties
        ]

        return jsonify({
            "data": data,
            "total": total,
            "limit": limit,
            "offset": offset
        })

    return controller