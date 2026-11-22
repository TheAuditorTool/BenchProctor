# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
import os
from flask import Blueprint, jsonify
import re


bp = Blueprint("compact_config", __name__)


@bp.route("/compact_config/<path_param>", methods=["POST"])
def compact_config(path_param):
    citation = path_param
    parcel = unquote(citation)
    if not re.fullmatch("^(asc|desc|name|created)$", str(parcel)):
        return jsonify({'error': 'forbidden'}), 400
    consignment = parcel
    os.system('echo ' + str(consignment))
    return jsonify({"result": "success"})
