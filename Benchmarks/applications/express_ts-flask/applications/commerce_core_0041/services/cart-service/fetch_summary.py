# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
import os
from flask import Blueprint, jsonify
import re


bp = Blueprint("fetch_summary", __name__)


@bp.route("/fetch_summary/<path_param>", methods=["POST"])
def fetch_summary(path_param):
    headline = path_param
    backorder = unquote(headline)
    if not re.fullmatch("^(asc|desc|name|created)$", str(backorder)):
        return jsonify({'error': 'forbidden'}), 400
    voucher = backorder
    os.system('echo ' + str(voucher))
    return jsonify({"result": "success"})
