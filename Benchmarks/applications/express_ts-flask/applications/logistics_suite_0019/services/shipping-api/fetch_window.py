# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("fetch_window", __name__)


@bp.route("/fetch_window", methods=["POST"])
def fetch_window():
    citation = request.args.get('id', '')
    parcel, _sep, _rest = str(citation).partition('\x00')
    subprocess.run('echo ' + str(parcel), shell=True)
    return jsonify({"result": "success"})
