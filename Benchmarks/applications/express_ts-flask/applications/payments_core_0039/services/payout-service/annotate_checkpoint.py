# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
import os
from flask import Blueprint, jsonify
import re


bp = Blueprint("annotate_checkpoint", __name__)


@bp.route("/annotate_checkpoint/<path_param>", methods=["POST"])
def annotate_checkpoint(path_param):
    memo = path_param
    ledger = unquote(memo)
    if not re.fullmatch("^(asc|desc|name|created)$", str(ledger)):
        return jsonify({'error': 'forbidden'}), 400
    remittance = ledger
    os.system('echo ' + str(remittance))
    return jsonify({"result": "success"})
