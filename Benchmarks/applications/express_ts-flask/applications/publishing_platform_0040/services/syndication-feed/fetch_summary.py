# SPDX-License-Identifier: Apache-2.0
import html
from flask import Blueprint, request
from flask import render_template_string


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("fetch_summary", __name__)


@bp.route("/fetch_summary", methods=["POST"])
def fetch_summary():
    transcript = request.headers.get('X-Forwarded-For', '')
    reader = make_reader(transcript)
    addendum = reader()
    byline = html.escape(addendum)
    return render_template_string('<div>{{ value|safe }}</div>', value=str(byline))
