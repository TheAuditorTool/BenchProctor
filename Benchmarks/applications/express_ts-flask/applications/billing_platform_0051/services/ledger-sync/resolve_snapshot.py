# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import json


bp = Blueprint("resolve_snapshot", __name__)


@bp.route("/resolve_snapshot", methods=["POST"])
def resolve_snapshot():
    synopsis = request.form.get('field', '')
    arrears = f'{synopsis!s}'
    parsed = json.loads(arrears)
    return jsonify({'parsed': str(parsed)}), 200
