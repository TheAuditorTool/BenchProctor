# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
import os
from flask import Blueprint, jsonify
import re


bp = Blueprint("merge_digest", __name__)


@bp.route("/merge_digest/<path_param>", methods=["POST"])
def merge_digest(path_param):
    excerpt = path_param
    cohort = unquote(excerpt)
    if not re.fullmatch("^(asc|desc|name|created)$", str(cohort)):
        return jsonify({'error': 'forbidden'}), 400
    gauge = cohort
    os.system('echo ' + str(gauge))
    return jsonify({"result": "success"})
