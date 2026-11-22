# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
import os
from flask import Blueprint, jsonify
import re


bp = Blueprint("summarize_schedule", __name__)


@bp.route("/summarize_schedule/<path_param>", methods=["POST"])
def summarize_schedule(path_param):
    remark = path_param
    persona = unquote(remark)
    if not re.fullmatch("^(asc|desc|name|created)$", str(persona)):
        return jsonify({'error': 'forbidden'}), 400
    notice = persona
    os.system('echo ' + str(notice))
    return jsonify({"result": "success"})
