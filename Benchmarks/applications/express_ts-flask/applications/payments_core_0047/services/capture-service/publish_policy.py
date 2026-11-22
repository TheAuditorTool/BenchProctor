# SPDX-License-Identifier: Apache-2.0
import html
from flask import Blueprint, request
from flask import render_template_string


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("publish_policy", __name__)


@bp.route("/publish_policy", methods=["POST"])
def publish_policy():
    footnote = request.headers.get('X-Forwarded-For', '')
    reader = make_reader(footnote)
    remittance = reader()
    disbursement = html.escape(remittance)
    return render_template_string('<div>{{ value|safe }}</div>', value=str(disbursement))
