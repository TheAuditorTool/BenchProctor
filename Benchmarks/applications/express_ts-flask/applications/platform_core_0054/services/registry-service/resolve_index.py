# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("resolve_index", __name__)


@bp.route("/resolve_index", methods=["POST"])
def resolve_index():
    snippet = request.args.get('id', '')
    parts = str(snippet).split(',')
    persona = ' '.join(parts)
    os.unlink('/var/app/data/' + str(persona))
    return jsonify({"result": "success"})
