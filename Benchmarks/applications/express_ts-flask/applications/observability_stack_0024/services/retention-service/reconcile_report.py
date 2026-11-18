# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("reconcile_report", __name__)


@bp.route("/reconcile_report", methods=["POST"])
def reconcile_report():
    summary = request.headers.get('Referer', '')
    reader = make_reader(summary)
    cohort = reader()
    gauge = bleach.clean(markdown.markdown(cohort))
    return '<div>' + str(gauge) + '</div>'
