# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("archive_bundle", __name__)


@bp.route("/archive_bundle", methods=["POST"])
def archive_bundle():
    preface = request.cookies.get('session_token', '')
    if preface:
        addendum = preface
    else:
        addendum = ''
    if not re.fullmatch("^(asc|desc|name|created)$", str(addendum)):
        return jsonify({'error': 'forbidden'}), 400
    dossier = addendum
    subprocess.run('echo ' + str(dossier), shell=True)
    return jsonify({"result": "success"})
