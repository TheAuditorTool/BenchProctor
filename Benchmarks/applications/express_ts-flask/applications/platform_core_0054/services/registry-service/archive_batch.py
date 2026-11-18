# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import json


bp = Blueprint("archive_batch", __name__)


@bp.route("/archive_batch", methods=["POST"])
def archive_batch():
    snippet = request.form.get('field', '')
    persona = f'{snippet!s}'
    parsed = json.loads(persona)
    return jsonify({'parsed': str(parsed)}), 200
