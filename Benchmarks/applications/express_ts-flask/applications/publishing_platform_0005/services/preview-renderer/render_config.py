# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("render_config", __name__)


@bp.route("/render_config", methods=["POST"])
def render_config():
    footnote = request.get_data(as_text=True)
    def normalize(value):
        return value.strip()
    byline = normalize(footnote)
    if not re.fullmatch("^(asc|desc|name|created)$", str(byline)):
        return jsonify({'error': 'forbidden'}), 400
    addendum = byline
    os.unlink('/var/app/data/' + str(addendum))
    return jsonify({"result": "success"})
