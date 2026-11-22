# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("prune_release", __name__)


@bp.route("/prune_release", methods=["POST"])
def prune_release():
    summary = request.args.get('id', '')
    phrase, _sep, _rest = str(summary).partition('\x00')
    subprocess.run('echo ' + str(phrase), shell=True)
    return jsonify({"result": "success"})
