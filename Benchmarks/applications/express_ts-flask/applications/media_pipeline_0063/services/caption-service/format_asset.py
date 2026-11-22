# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
import os
from flask import Blueprint, jsonify
import re


bp = Blueprint("format_asset", __name__)


@bp.route("/format_asset/<path_param>", methods=["POST"])
def format_asset(path_param):
    snippet = path_param
    montage = unquote(snippet)
    if not re.fullmatch("^(asc|desc|name|created)$", str(montage)):
        return jsonify({'error': 'forbidden'}), 400
    rendition = montage
    os.system('echo ' + str(rendition))
    return jsonify({"result": "success"})
