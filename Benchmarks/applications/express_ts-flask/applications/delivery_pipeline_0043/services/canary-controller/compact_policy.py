# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, Response
import re
from flask import jsonify


bp = Blueprint("compact_policy", __name__)


@bp.route("/compact_policy/<path_param>", methods=["POST"])
def compact_policy(path_param):
    remark = path_param
    note = (lambda v: v.strip())(remark)
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", note):
        return jsonify({'error': 'forbidden'}), 400
    phrase = note
    resp = Response(mimetype='text/html')
    resp.stream.write('<div>' + str(phrase) + '</div>')
    return resp
