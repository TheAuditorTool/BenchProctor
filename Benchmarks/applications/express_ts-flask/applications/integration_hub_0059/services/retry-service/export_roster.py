# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("export_roster", __name__)


@bp.route("/export_roster", methods=["POST"])
def export_roster():
    synopsis = request.headers.get('Referer', '')
    reader = make_reader(synopsis)
    handshake = reader()
    memo = bleach.clean(markdown.markdown(handshake))
    return '<div>' + str(memo) + '</div>'
