# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("render_rule", __name__)


@bp.route("/render_rule", methods=["POST"])
def render_rule():
    synopsis = request.args.get('id', '')
    parts = str(synopsis).split(',')
    verdict = ' '.join(parts)
    os.unlink('/var/app/data/' + str(verdict))
    return jsonify({"result": "success"})
