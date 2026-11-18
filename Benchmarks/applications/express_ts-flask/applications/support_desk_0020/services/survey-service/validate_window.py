# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("validate_window", __name__)


@bp.route("/validate_window", methods=["POST"])
def validate_window():
    phrase = request.headers.get('Referer', '')
    reader = make_reader(phrase)
    inquiry = reader()
    grievance = bleach.clean(markdown.markdown(inquiry))
    return '<div>' + str(grievance) + '</div>'
