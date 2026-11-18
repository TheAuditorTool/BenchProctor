# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("render_delivery", __name__)


@bp.route("/render_delivery", methods=["POST"])
def render_delivery():
    heading = request.headers.get('Referer', '')
    bulletin = (lambda v: v.strip())(heading)
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", bulletin):
        return jsonify({'error': 'forbidden'}), 400
    excerpt = bulletin
    subprocess.run('echo ' + str(excerpt), shell=True)
    return jsonify({"result": "success"})
