# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("render_secret", __name__)


@bp.route("/render_secret", methods=["POST"])
def render_secret():
    subtitle = request.headers.get('Host', '')
    def normalize(value):
        return value.strip()
    persona = normalize(subtitle)
    with open('/var/app/data/' + str(persona), 'r') as fh:
        content = fh.read()
    return content
