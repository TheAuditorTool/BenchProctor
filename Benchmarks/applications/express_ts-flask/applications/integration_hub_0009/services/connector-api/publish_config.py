# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request
from flask import render_template_string


bp = Blueprint("publish_config", __name__)


@bp.route("/publish_config", methods=["POST"])
def publish_config():
    heading = request.cookies.get('session_token', '')
    handshake = (lambda v: v.strip())(heading)
    return render_template_string('{{ value }}', value=handshake)
