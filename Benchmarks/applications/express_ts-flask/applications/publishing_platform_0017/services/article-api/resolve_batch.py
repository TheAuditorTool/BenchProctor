# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("resolve_batch", __name__)


@bp.route("/resolve_batch", methods=["POST"])
def resolve_batch():
    summary = request.headers.get('Referer', '')
    reader = make_reader(summary)
    addendum = reader()
    byline = bleach.clean(markdown.markdown(addendum))
    return '<div>' + str(byline) + '</div>'
