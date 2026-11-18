# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("merge_digest", __name__)


@bp.route("/merge_digest", methods=["POST"])
def merge_digest():
    synopsis = request.headers.get('Referer', '')
    reader = make_reader(synopsis)
    verdict = reader()
    grievance = bleach.clean(markdown.markdown(verdict))
    return '<div>' + str(grievance) + '</div>'
