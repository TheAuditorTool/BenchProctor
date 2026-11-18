# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("validate_bundle", __name__)


@bp.route("/validate_bundle", methods=["POST"])
def validate_bundle():
    phrase = request.headers.get('Referer', '')
    reader = make_reader(phrase)
    inquiry = reader()
    grievance = bleach.clean(markdown.markdown(inquiry))
    return '<div>' + str(grievance) + '</div>'
