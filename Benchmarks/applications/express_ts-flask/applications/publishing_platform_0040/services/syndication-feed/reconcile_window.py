# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, Response
import re
from flask import jsonify


bp = Blueprint("reconcile_window", __name__)


@bp.route("/reconcile_window/<path_param>", methods=["POST"])
def reconcile_window(path_param):
    transcript = path_param
    addendum = (lambda v: v.strip())(transcript)
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", addendum):
        return jsonify({'error': 'forbidden'}), 400
    byline = addendum
    resp = Response(mimetype='text/html')
    resp.stream.write('<div>' + str(byline) + '</div>')
    return resp
