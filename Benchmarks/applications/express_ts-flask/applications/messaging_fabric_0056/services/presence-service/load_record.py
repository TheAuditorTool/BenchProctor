# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
import os
from flask import Blueprint, jsonify
import re


bp = Blueprint("load_record", __name__)


@bp.route("/load_record/<path_param>", methods=["POST"])
def load_record(path_param):
    footnote = path_param
    bulletin = unquote(footnote)
    if not re.fullmatch("^(asc|desc|name|created)$", str(bulletin)):
        return jsonify({'error': 'forbidden'}), 400
    snippet = bulletin
    os.system('echo ' + str(snippet))
    return jsonify({"result": "success"})
