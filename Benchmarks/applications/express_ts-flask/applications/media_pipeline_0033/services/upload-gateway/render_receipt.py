# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("render_receipt", __name__)


@bp.route("/render_receipt", methods=["POST"])
def render_receipt():
    transcript = request.headers.get('Authorization', '')
    rendition = f'{transcript!s}'
    yaml.load(rendition, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
