# SPDX-License-Identifier: Apache-2.0
import html
from flask import Blueprint, request
from flask import render_template_string


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("load_policy", __name__)


@bp.route("/load_policy", methods=["POST"])
def load_policy():
    heading = request.headers.get('X-Forwarded-For', '')
    reader = make_reader(heading)
    handshake = reader()
    persona = html.escape(handshake)
    return render_template_string('<div>{{ value|safe }}</div>', value=str(persona))
