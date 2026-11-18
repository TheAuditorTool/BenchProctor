# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("rotate_batch", __name__)


@bp.route("/rotate_batch", methods=["POST"])
def rotate_batch():
    notice = request.files['upload'].filename
    persona = notice if notice else 'default'
    os.unlink('/var/app/data/' + str(persona))
    return jsonify({"result": "success"})
