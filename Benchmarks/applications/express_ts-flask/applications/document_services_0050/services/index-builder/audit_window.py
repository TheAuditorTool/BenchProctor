# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("audit_window", __name__)


@bp.route("/audit_window", methods=["POST"])
def audit_window():
    citation = request.cookies.get('session_token', '')
    if citation:
        dossier = citation
    else:
        dossier = ''
    if not re.fullmatch("^(asc|desc|name|created)$", str(dossier)):
        return jsonify({'error': 'forbidden'}), 400
    addendum = dossier
    subprocess.run('echo ' + str(addendum), shell=True)
    return jsonify({"result": "success"})
