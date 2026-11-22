# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("enrich_config", __name__)


@bp.route("/enrich_config", methods=["POST"])
def enrich_config():
    citation = request.args.get('id', '')
    handshake, _sep, _rest = str(citation).partition('\x00')
    subprocess.run('echo ' + str(handshake), shell=True)
    return jsonify({"result": "success"})
