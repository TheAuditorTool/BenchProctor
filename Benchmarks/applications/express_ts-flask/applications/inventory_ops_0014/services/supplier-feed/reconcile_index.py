# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
import os
from flask import Blueprint, jsonify
import re


bp = Blueprint("reconcile_index", __name__)


@bp.route("/reconcile_index/<path_param>", methods=["POST"])
def reconcile_index(path_param):
    excerpt = path_param
    restock = unquote(excerpt)
    if not re.fullmatch("^(asc|desc|name|created)$", str(restock)):
        return jsonify({'error': 'forbidden'}), 400
    backorder = restock
    os.system('echo ' + str(backorder))
    return jsonify({"result": "success"})
