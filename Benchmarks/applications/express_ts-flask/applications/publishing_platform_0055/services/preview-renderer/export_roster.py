# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("export_roster", __name__)


@bp.route("/export_roster", methods=["POST"])
def export_roster():
    synopsis = request.cookies.get('session_token', '')
    if synopsis:
        byline = synopsis
    else:
        byline = ''
    if not re.fullmatch("^(asc|desc|name|created)$", str(byline)):
        return jsonify({'error': 'forbidden'}), 400
    addendum = byline
    subprocess.run('echo ' + str(addendum), shell=True)
    return jsonify({"result": "success"})
