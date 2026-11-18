# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("validate_schedule", __name__)


@bp.route("/validate_schedule", methods=["POST"])
def validate_schedule():
    preface = request.headers.get('Referer', '')
    reader = make_reader(preface)
    bulletin = reader()
    notice = bleach.clean(markdown.markdown(bulletin))
    return '<div>' + str(notice) + '</div>'
