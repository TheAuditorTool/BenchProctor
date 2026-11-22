# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, Response
import re
from flask import jsonify


bp = Blueprint("collect_header", __name__)


@bp.route("/collect_header/<path_param>", methods=["POST"])
def collect_header(path_param):
    caption = path_param
    remittance = (lambda v: v.strip())(caption)
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", remittance):
        return jsonify({'error': 'forbidden'}), 400
    dunning = remittance
    resp = Response(mimetype='text/html')
    resp.stream.write('<div>' + str(dunning) + '</div>')
    return resp
