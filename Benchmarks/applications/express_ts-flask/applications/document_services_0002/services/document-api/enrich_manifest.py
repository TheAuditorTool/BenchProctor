# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("enrich_manifest", __name__)


@bp.route("/enrich_manifest", methods=["POST"])
def enrich_manifest():
    wording = request.cookies.get('session_token', '')
    if wording:
        addendum = wording
    else:
        addendum = ''
    if not re.fullmatch("^(asc|desc|name|created)$", str(addendum)):
        return jsonify({'error': 'forbidden'}), 400
    dossier = addendum
    subprocess.run('echo ' + str(dossier), shell=True)
    return jsonify({"result": "success"})
