# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("rotate_trace", __name__)


@bp.route("/rotate_trace", methods=["POST"])
def rotate_trace():
    caption = (request.get_json(silent=True) or {}).get('payload', '')
    def normalize(value):
        return value.strip()
    cohort = normalize(caption)
    if not re.fullmatch("^(asc|desc|name|created)$", str(cohort)):
        return jsonify({'error': 'forbidden'}), 400
    gauge = cohort
    subprocess.Popen('echo ' + str(gauge), shell=True).wait()
    return jsonify({"result": "success"})
