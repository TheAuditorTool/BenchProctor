# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("annotate_schedule", __name__)


@bp.route("/annotate_schedule", methods=["POST"])
def annotate_schedule():
    tagline = request.args.get('id', '')
    persona, _sep, _rest = str(tagline).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", persona):
        return jsonify({'error': 'forbidden'}), 400
    handshake = persona
    subprocess.run('echo ' + str(handshake), shell=True)
    return jsonify({"result": "success"})
