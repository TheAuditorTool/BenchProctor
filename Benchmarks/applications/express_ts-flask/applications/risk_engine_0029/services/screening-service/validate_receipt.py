# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("validate_receipt", __name__)


@bp.route("/validate_receipt", methods=["POST"])
def validate_receipt():
    subject = request.files['upload'].filename
    grievance = subject if subject else 'default'
    os.unlink('/var/app/data/' + str(grievance))
    return jsonify({"result": "success"})
