# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
import os
from flask import Blueprint, jsonify
import re


bp = Blueprint("validate_window", __name__)


@bp.route("/validate_window/<path_param>", methods=["POST"])
def validate_window(path_param):
    memo = path_param
    backorder = unquote(memo)
    if not re.fullmatch("^(asc|desc|name|created)$", str(backorder)):
        return jsonify({'error': 'forbidden'}), 400
    restock = backorder
    os.system('echo ' + str(restock))
    return jsonify({"result": "success"})
