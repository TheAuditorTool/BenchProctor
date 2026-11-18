# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("format_window", __name__)


@bp.route("/format_window", methods=["POST"])
def format_window():
    subtitle = request.form.get('field', '')
    ledger = unquote(subtitle)
    subprocess.run('echo ' + str(ledger), shell=True)
    return jsonify({"result": "success"})
