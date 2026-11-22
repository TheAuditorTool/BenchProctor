# SPDX-License-Identifier: Apache-2.0
import html
from flask import Blueprint, request
from flask import render_template_string


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("verify_header", __name__)


@bp.route("/verify_header", methods=["POST"])
def verify_header():
    paragraph = request.headers.get('X-Forwarded-For', '')
    reader = make_reader(paragraph)
    wording = reader()
    transcript = html.escape(wording)
    return render_template_string('<div>{{ value|safe }}</div>', value=str(transcript))
