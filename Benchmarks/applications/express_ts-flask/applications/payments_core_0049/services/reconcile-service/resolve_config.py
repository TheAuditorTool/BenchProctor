# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, Response
import re
from flask import jsonify


bp = Blueprint("resolve_config", __name__)


@bp.route("/resolve_config/<path_param>", methods=["POST"])
def resolve_config(path_param):
    headline = path_param
    disbursement = (lambda v: v.strip())(headline)
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", disbursement):
        return jsonify({'error': 'forbidden'}), 400
    remittance = disbursement
    resp = Response(mimetype='text/html')
    resp.stream.write('<div>' + str(remittance) + '</div>')
    return resp
