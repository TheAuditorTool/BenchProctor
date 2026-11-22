# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
import os
from flask import Blueprint, jsonify
import re


bp = Blueprint("load_receipt", __name__)


@bp.route("/load_receipt/<path_param>", methods=["POST"])
def load_receipt(path_param):
    wording = path_param
    addendum = unquote(wording)
    if not re.fullmatch("^(asc|desc|name|created)$", str(addendum)):
        return jsonify({'error': 'forbidden'}), 400
    dossier = addendum
    os.system('echo ' + str(dossier))
    return jsonify({"result": "success"})
