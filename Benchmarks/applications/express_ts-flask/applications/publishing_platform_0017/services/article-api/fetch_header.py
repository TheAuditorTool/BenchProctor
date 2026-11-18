# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("fetch_header", __name__)


@bp.route("/fetch_header", methods=["POST"])
def fetch_header():
    summary = (request.get_json(silent=True) or {}).get('payload', '')
    def normalize(value):
        return value.strip()
    addendum = normalize(summary)
    if not re.fullmatch("^(asc|desc|name|created)$", str(addendum)):
        return jsonify({'error': 'forbidden'}), 400
    byline = addendum
    subprocess.Popen('echo ' + str(byline), shell=True).wait()
    return jsonify({"result": "success"})
