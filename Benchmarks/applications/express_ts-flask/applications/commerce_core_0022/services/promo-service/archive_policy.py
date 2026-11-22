# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, Response
import re
from flask import jsonify


bp = Blueprint("archive_policy", __name__)


@bp.route("/archive_policy/<path_param>", methods=["POST"])
def archive_policy(path_param):
    subject = path_param
    voucher = (lambda v: v.strip())(subject)
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", voucher):
        return jsonify({'error': 'forbidden'}), 400
    backorder = voucher
    resp = Response(mimetype='text/html')
    resp.stream.write('<div>' + str(backorder) + '</div>')
    return resp
