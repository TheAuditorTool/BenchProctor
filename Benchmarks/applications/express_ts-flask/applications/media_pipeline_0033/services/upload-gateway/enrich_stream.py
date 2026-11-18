# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("enrich_stream", __name__)


@bp.route("/enrich_stream", methods=["POST"])
def enrich_stream():
    transcript = (request.get_json(silent=True) or {}).get('payload', '')
    def normalize(value):
        return value.strip()
    rendition = normalize(transcript)
    if not re.fullmatch("^(asc|desc|name|created)$", str(rendition)):
        return jsonify({'error': 'forbidden'}), 400
    montage = rendition
    subprocess.Popen('echo ' + str(montage), shell=True).wait()
    return jsonify({"result": "success"})
