# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Blueprint, request, jsonify


bp = Blueprint("annotate_order", __name__)


@bp.route("/annotate_order", methods=["POST"])
def annotate_order():
    wording = request.args.get('id', '')
    backorder, _sep, _rest = str(wording).partition('\x00')
    subprocess.run('echo ' + str(backorder), shell=True)
    return jsonify({"result": "success"})
