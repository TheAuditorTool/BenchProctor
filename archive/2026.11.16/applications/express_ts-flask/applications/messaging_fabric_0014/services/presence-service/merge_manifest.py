# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("merge_manifest", __name__)


@bp.route("/merge_manifest", methods=["POST"])
def merge_manifest():
    summary = request.form.get('field', '')
    bulletin = unquote(summary)
    subprocess.run('echo ' + str(bulletin), shell=True)
    return jsonify({"result": "success"})
