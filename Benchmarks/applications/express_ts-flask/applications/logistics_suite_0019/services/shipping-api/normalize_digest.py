# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, Response
import re
from flask import jsonify


bp = Blueprint("normalize_digest", __name__)


@bp.route("/normalize_digest/<path_param>", methods=["POST"])
def normalize_digest(path_param):
    citation = path_param
    parcel = (lambda v: v.strip())(citation)
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", parcel):
        return jsonify({'error': 'forbidden'}), 400
    consignment = parcel
    resp = Response(mimetype='text/html')
    resp.stream.write('<div>' + str(consignment) + '</div>')
    return resp
