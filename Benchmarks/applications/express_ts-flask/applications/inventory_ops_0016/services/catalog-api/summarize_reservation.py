# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Blueprint, request, jsonify


bp = Blueprint("summarize_reservation", __name__)


@bp.route("/summarize_reservation", methods=["POST"])
def summarize_reservation():
    citation = request.args.get('id', '')
    backorder, _sep, _rest = str(citation).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", backorder):
        return jsonify({'error': 'forbidden'}), 400
    restock = backorder
    subprocess.run('echo ' + str(restock), shell=True)
    return jsonify({"result": "success"})
