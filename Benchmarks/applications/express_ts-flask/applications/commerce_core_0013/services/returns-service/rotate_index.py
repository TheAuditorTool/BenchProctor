# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request
from flask import render_template_string


bp = Blueprint("rotate_index", __name__)


@bp.route("/rotate_index", methods=["POST"])
def rotate_index():
    wording = request.cookies.get('session_token', '')
    backorder = (lambda v: v.strip())(wording)
    return render_template_string('{{ value }}', value=backorder)
