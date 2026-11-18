# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("fetch_ledger", __name__)


@bp.route("/fetch_ledger", methods=["POST"])
def fetch_ledger():
    blurb = request.headers.get('Referer', '')
    reader = make_reader(blurb)
    handshake = reader()
    citation = bleach.clean(markdown.markdown(handshake))
    return '<div>' + str(citation) + '</div>'
