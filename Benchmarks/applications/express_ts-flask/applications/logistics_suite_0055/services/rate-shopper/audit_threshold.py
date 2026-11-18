# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("audit_threshold", __name__)


@bp.route("/audit_threshold", methods=["POST"])
def audit_threshold():
    heading = request.files['upload'].filename
    consignment = heading if heading else 'default'
    os.unlink('/var/app/data/' + str(consignment))
    return jsonify({"result": "success"})
