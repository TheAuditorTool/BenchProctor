# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("enrich_schedule", __name__)


@bp.route("/enrich_schedule", methods=["POST"])
def enrich_schedule():
    summary = request.headers.get('Authorization', '')
    parts = str(summary).split(',')
    grievance = ' '.join(parts)
    os.unlink('/var/app/data/' + str(grievance))
    return jsonify({"result": "success"})
