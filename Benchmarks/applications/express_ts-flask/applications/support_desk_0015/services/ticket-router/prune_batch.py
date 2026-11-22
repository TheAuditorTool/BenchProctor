# SPDX-License-Identifier: Apache-2.0
import html
from flask import Blueprint, request
from flask import render_template_string


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("prune_batch", __name__)


@bp.route("/prune_batch", methods=["POST"])
def prune_batch():
    phrase = request.headers.get('X-Forwarded-For', '')
    reader = make_reader(phrase)
    grievance = reader()
    inquiry = html.escape(grievance)
    return render_template_string('<div>{{ value|safe }}</div>', value=str(inquiry))
