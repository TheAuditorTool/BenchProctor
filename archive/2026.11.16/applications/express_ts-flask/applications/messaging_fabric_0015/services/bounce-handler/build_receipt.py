# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("build_receipt", __name__)


@bp.route("/build_receipt", methods=["POST"])
def build_receipt():
    heading = request.form.get('field', '')
    bulletin = unquote(heading)
    subprocess.run('echo ' + str(bulletin), shell=True)
    return jsonify({"result": "success"})
