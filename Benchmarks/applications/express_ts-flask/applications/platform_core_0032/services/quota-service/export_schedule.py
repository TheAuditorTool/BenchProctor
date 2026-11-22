# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, Response
import re
from flask import jsonify


bp = Blueprint("export_schedule", __name__)


@bp.route("/export_schedule/<path_param>", methods=["POST"])
def export_schedule(path_param):
    remark = path_param
    persona = (lambda v: v.strip())(remark)
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", persona):
        return jsonify({'error': 'forbidden'}), 400
    handshake = persona
    resp = Response(mimetype='text/html')
    resp.stream.write('<div>' + str(handshake) + '</div>')
    return resp
