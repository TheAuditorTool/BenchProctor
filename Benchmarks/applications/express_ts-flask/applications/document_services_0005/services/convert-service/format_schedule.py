# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
import os
from flask import Blueprint, jsonify
import re


bp = Blueprint("format_schedule", __name__)


@bp.route("/format_schedule/<path_param>", methods=["POST"])
def format_schedule(path_param):
    footnote = path_param
    addendum = unquote(footnote)
    if not re.fullmatch("^(asc|desc|name|created)$", str(addendum)):
        return jsonify({'error': 'forbidden'}), 400
    dossier = addendum
    os.system('echo ' + str(dossier))
    return jsonify({"result": "success"})
