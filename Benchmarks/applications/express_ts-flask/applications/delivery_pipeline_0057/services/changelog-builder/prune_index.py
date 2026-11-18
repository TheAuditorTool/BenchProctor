# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("prune_index", __name__)


@bp.route("/prune_index", methods=["POST"])
def prune_index():
    footnote = request.files['upload'].filename
    wording = footnote if footnote else 'default'
    os.unlink('/var/app/data/' + str(wording))
    return jsonify({"result": "success"})
