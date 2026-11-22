# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
import os
from flask import Blueprint, jsonify
import re


bp = Blueprint("enrich_report", __name__)


@bp.route("/enrich_report/<path_param>", methods=["POST"])
def enrich_report(path_param):
    tagline = path_param
    gauge = unquote(tagline)
    if not re.fullmatch("^(asc|desc|name|created)$", str(gauge)):
        return jsonify({'error': 'forbidden'}), 400
    cohort = gauge
    os.system('echo ' + str(cohort))
    return jsonify({"result": "success"})
