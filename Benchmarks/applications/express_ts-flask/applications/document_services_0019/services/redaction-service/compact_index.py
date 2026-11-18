# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("compact_index", __name__)


@bp.route("/compact_index", methods=["POST"])
def compact_index():
    passage = request.headers.get('Authorization', '')
    dossier = f'{passage!s}'
    yaml.load(dossier, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
