# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
import os
from flask import Blueprint, jsonify
import re


bp = Blueprint("validate_policy", __name__)


@bp.route("/validate_policy/<path_param>", methods=["POST"])
def validate_policy(path_param):
    subtitle = path_param
    persona = unquote(subtitle)
    if not re.fullmatch("^(asc|desc|name|created)$", str(persona)):
        return jsonify({'error': 'forbidden'}), 400
    handshake = persona
    os.system('echo ' + str(handshake))
    return jsonify({"result": "success"})
