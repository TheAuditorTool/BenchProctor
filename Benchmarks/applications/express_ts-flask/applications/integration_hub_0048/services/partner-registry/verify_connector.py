# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, Response
import re
from flask import jsonify


bp = Blueprint("verify_connector", __name__)


@bp.route("/verify_connector/<path_param>", methods=["POST"])
def verify_connector(path_param):
    citation = path_param
    handshake = (lambda v: v.strip())(citation)
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", handshake):
        return jsonify({'error': 'forbidden'}), 400
    heading = handshake
    resp = Response(mimetype='text/html')
    resp.stream.write('<div>' + str(heading) + '</div>')
    return resp
