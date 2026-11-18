# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import json


bp = Blueprint("fetch_window", __name__)


@bp.route("/fetch_window", methods=["POST"])
def fetch_window():
    notice = request.form.get('field', '')
    rendition = f'{notice!s}'
    parsed = json.loads(rendition)
    return jsonify({'parsed': str(parsed)}), 200
