# SPDX-License-Identifier: Apache-2.0
import html
from flask import Blueprint, request
from flask import render_template_string


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("audit_digest", __name__)


@bp.route("/audit_digest", methods=["POST"])
def audit_digest():
    remark = request.headers.get('X-Forwarded-For', '')
    reader = make_reader(remark)
    persona = reader()
    notice = html.escape(persona)
    return render_template_string('<div>{{ value|safe }}</div>', value=str(notice))
