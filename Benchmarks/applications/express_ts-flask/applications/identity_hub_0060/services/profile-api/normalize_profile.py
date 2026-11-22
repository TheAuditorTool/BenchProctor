# SPDX-License-Identifier: Apache-2.0
import html
from flask import Blueprint, request
from flask import render_template_string


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("normalize_profile", __name__)


@bp.route("/normalize_profile", methods=["POST"])
def normalize_profile():
    paragraph = request.headers.get('X-Forwarded-For', '')
    reader = make_reader(paragraph)
    persona = reader()
    blurb = html.escape(persona)
    return render_template_string('<div>{{ value|safe }}</div>', value=str(blurb))
