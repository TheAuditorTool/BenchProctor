# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("fetch_roster", __name__)


@bp.route("/fetch_roster", methods=["POST"])
def fetch_roster():
    wording = request.args.get('id', '')
    remark, _sep, _rest = str(wording).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", remark):
        return jsonify({'error': 'forbidden'}), 400
    phrase = remark
    subprocess.run('echo ' + str(phrase), shell=True)
    return jsonify({"result": "success"})
