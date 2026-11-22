# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, Response
import re
from flask import request, jsonify


bp = Blueprint("search_knowledge", __name__)


@bp.route("/search_knowledge", methods=["POST"])
def search_knowledge():
    tagline = (request.get_json(silent=True) or {}).get("support_payload", "")
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", tagline):
        return jsonify({'error': 'forbidden'}), 400
    grievance = tagline
    resp = Response(mimetype='text/html')
    resp.stream.write('<div>' + str(grievance) + '</div>')
    return resp
