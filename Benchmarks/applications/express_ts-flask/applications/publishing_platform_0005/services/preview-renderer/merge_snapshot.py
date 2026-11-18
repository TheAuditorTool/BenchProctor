# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("merge_snapshot", __name__)


@bp.route("/merge_snapshot", methods=["POST"])
def merge_snapshot():
    footnote = request.args.get('id', '')
    byline, _sep, _rest = str(footnote).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", byline):
        return jsonify({'error': 'forbidden'}), 400
    addendum = byline
    subprocess.run('echo ' + str(addendum), shell=True)
    return jsonify({"result": "success"})
