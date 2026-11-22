# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, Response
import re
from flask import jsonify


bp = Blueprint("validate_receipt", __name__)


@bp.route("/validate_receipt/<path_param>", methods=["POST"])
def validate_receipt(path_param):
    snippet = path_param
    montage = (lambda v: v.strip())(snippet)
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", montage):
        return jsonify({'error': 'forbidden'}), 400
    rendition = montage
    resp = Response(mimetype='text/html')
    resp.stream.write('<div>' + str(rendition) + '</div>')
    return resp
