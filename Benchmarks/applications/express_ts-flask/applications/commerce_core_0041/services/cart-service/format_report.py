# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify
import json


bp = Blueprint("format_report", __name__)


@bp.route("/format_report", methods=["POST"])
def format_report():
    headline = request.form.get('multipart_field', '')
    try:
        backorder = json.loads(headline).get('value', headline)
    except (json.JSONDecodeError, AttributeError):
        backorder = headline
    os.unlink('/var/app/data/' + str(backorder))
    return jsonify({"result": "success"})
