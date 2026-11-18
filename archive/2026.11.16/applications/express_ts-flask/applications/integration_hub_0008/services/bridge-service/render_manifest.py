# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


bp = Blueprint("render_manifest", __name__)


@bp.route("/render_manifest", methods=["POST"])
def render_manifest():
    preface = request.headers.get('X-Custom-Header', '')
    def normalize(value):
        return value.strip()
    handshake = normalize(preface)
    paragraph = bleach.clean(markdown.markdown(handshake))
    return '<div>' + str(paragraph) + '</div>'
