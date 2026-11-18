# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("normalize_window", __name__)


@bp.route("/normalize_window", methods=["POST"])
def normalize_window():
    footnote = request.headers.get('Referer', '')
    reader = make_reader(footnote)
    handshake = reader()
    blurb = bleach.clean(markdown.markdown(handshake))
    return '<div>' + str(blurb) + '</div>'
