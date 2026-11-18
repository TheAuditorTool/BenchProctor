# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("load_bundle", __name__)


@bp.route("/load_bundle", methods=["POST"])
def load_bundle():
    synopsis = request.get_data(as_text=True)
    def normalize(value):
        return value.strip()
    handshake = normalize(synopsis)
    if not re.fullmatch("^(asc|desc|name|created)$", str(handshake)):
        return jsonify({'error': 'forbidden'}), 400
    memo = handshake
    os.unlink('/var/app/data/' + str(memo))
    return jsonify({"result": "success"})
