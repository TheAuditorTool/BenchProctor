# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("enrich_batch", __name__)


@bp.route("/enrich_batch", methods=["POST"])
def enrich_batch():
    preface = request.cookies.get('session_token', '')
    if preface:
        grievance = preface
    else:
        grievance = ''
    if not re.fullmatch("^(asc|desc|name|created)$", str(grievance)):
        return jsonify({'error': 'forbidden'}), 400
    inquiry = grievance
    subprocess.run('echo ' + str(inquiry), shell=True)
    return jsonify({"result": "success"})
