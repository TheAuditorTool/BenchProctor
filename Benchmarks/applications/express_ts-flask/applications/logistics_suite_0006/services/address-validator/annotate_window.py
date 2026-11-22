# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, Response
import re
from flask import jsonify


bp = Blueprint("annotate_window", __name__)


@bp.route("/annotate_window/<path_param>", methods=["POST"])
def annotate_window(path_param):
    summary = path_param
    consignment = (lambda v: v.strip())(summary)
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", consignment):
        return jsonify({'error': 'forbidden'}), 400
    parcel = consignment
    resp = Response(mimetype='text/html')
    resp.stream.write('<div>' + str(parcel) + '</div>')
    return resp
