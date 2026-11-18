# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("audit_config", __name__)


@bp.route("/audit_config", methods=["POST"])
def audit_config():
    summary = request.headers.get('Referer', '')
    reader = make_reader(summary)
    gauge = reader()
    cohort = bleach.clean(markdown.markdown(gauge))
    return '<div>' + str(cohort) + '</div>'
