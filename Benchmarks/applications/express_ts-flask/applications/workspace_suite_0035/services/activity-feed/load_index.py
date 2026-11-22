# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("load_index", __name__)


@bp.route("/load_index", methods=["POST"])
def load_index():
    paragraph = (request.get_json(silent=True) or {}).get('payload', '')
    wording = paragraph if paragraph else 'default'
    os.system('echo ' + str(wording))
    return jsonify({"result": "success"})
