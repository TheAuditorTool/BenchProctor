# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("enrich_digest", __name__)


@bp.route("/enrich_digest", methods=["POST"])
def enrich_digest():
    phrase = request.headers.get('Referer', '')
    inquiry = (lambda v: v.strip())(phrase)
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", inquiry):
        return jsonify({'error': 'forbidden'}), 400
    grievance = inquiry
    subprocess.run('echo ' + str(grievance), shell=True)
    return jsonify({"result": "success"})
