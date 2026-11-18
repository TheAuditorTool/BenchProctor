# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Blueprint, request, jsonify


bp = Blueprint("load_profile", __name__)


@bp.route("/load_profile", methods=["POST"])
def load_profile():
    subject = request.files['upload'].filename
    parcel = f'{subject!s}'
    requests.get(str(parcel))
    return jsonify({"result": "success"})
