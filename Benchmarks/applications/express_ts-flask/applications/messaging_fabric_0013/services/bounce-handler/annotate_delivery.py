# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import json


bp = Blueprint("annotate_delivery", __name__)


@bp.route("/annotate_delivery", methods=["POST"])
def annotate_delivery():
    summary = request.form.get('field', '')
    bulletin = f'{summary!s}'
    parsed = json.loads(bulletin)
    return jsonify({'parsed': str(parsed)}), 200
