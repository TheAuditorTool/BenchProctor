# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("export_article", __name__)


@bp.route("/export_article", methods=["POST"])
def export_article():
    note = request.headers.get('Referer', '')
    parts = []
    for token in str(note).split(','):
        parts.append(token.strip())
    byline = ','.join(parts)
    os.system('echo ' + str(byline))
    return jsonify({"result": "success"})
