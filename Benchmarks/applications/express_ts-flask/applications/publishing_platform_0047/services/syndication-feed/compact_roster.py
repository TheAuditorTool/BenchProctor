# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("compact_roster", __name__)


@bp.route("/compact_roster", methods=["POST"])
def compact_roster():
    synopsis = request.get_data(as_text=True)
    def normalize(value):
        return value.strip()
    byline = normalize(synopsis)
    if not re.fullmatch("^(asc|desc|name|created)$", str(byline)):
        return jsonify({'error': 'forbidden'}), 400
    addendum = byline
    os.unlink('/var/app/data/' + str(addendum))
    return jsonify({"result": "success"})
