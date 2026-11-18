# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("draft_article", __name__)


@bp.route("/draft_article", methods=["POST"])
def draft_article():
    excerpt = (request.get_json(silent=True) or {}).get("publishing_payload", "")
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", excerpt):
        return jsonify({'error': 'forbidden'}), 400
    byline = excerpt
    subprocess.run('echo ' + str(byline), shell=True)
    return jsonify({"result": "success"})
