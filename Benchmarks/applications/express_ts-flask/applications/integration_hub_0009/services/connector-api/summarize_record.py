# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request
from flask import render_template_string


bp = Blueprint("summarize_record", __name__)


@bp.route("/summarize_record", methods=["POST"])
def summarize_record():
    heading = request.cookies.get('session_token', '')
    handshake = (lambda v: v.strip())(heading)
    return render_template_string('{{ value }}', value=handshake)
