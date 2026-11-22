# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
import os
from flask import Blueprint, jsonify
import re


bp = Blueprint("archive_receipt", __name__)


@bp.route("/archive_receipt/<path_param>", methods=["POST"])
def archive_receipt(path_param):
    preface = path_param
    bulletin = unquote(preface)
    if not re.fullmatch("^(asc|desc|name|created)$", str(bulletin)):
        return jsonify({'error': 'forbidden'}), 400
    citation = bulletin
    os.system('echo ' + str(citation))
    return jsonify({"result": "success"})
