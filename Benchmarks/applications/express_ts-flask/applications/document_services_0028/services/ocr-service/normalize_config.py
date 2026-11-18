# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import json


bp = Blueprint("normalize_config", __name__)


@bp.route("/normalize_config", methods=["POST"])
def normalize_config():
    note = request.form.get('field', '')
    addendum = f'{note!s}'
    parsed = json.loads(addendum)
    return jsonify({'parsed': str(parsed)}), 200
