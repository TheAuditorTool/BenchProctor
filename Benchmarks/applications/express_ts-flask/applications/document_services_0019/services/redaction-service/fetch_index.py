# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import json


bp = Blueprint("fetch_index", __name__)


@bp.route("/fetch_index", methods=["POST"])
def fetch_index():
    passage = request.form.get('field', '')
    dossier = f'{passage!s}'
    parsed = json.loads(dossier)
    return jsonify({'parsed': str(parsed)}), 200
