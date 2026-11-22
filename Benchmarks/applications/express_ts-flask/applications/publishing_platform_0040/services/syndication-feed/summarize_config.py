# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("summarize_config", __name__)


@bp.route("/summarize_config", methods=["POST"])
def summarize_config():
    transcript = request.form.get('field', '')
    parts = []
    for token in str(transcript).split(','):
        parts.append(token.strip())
    addendum = ','.join(parts)
    subprocess.run(['echo', addendum], shell=False)
    return jsonify({"result": "success"})
