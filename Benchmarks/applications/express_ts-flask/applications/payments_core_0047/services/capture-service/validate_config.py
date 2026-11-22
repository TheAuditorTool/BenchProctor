# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, Response
import re
from flask import jsonify


bp = Blueprint("validate_config", __name__)


@bp.route("/validate_config/<path_param>", methods=["POST"])
def validate_config(path_param):
    footnote = path_param
    remittance = (lambda v: v.strip())(footnote)
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", remittance):
        return jsonify({'error': 'forbidden'}), 400
    disbursement = remittance
    resp = Response(mimetype='text/html')
    resp.stream.write('<div>' + str(disbursement) + '</div>')
    return resp
