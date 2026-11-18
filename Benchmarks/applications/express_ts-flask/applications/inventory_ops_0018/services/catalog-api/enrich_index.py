# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("enrich_index", __name__)


@bp.route("/enrich_index", methods=["POST"])
def enrich_index():
    transcript = request.headers.get('Referer', '')
    reader = make_reader(transcript)
    backorder = reader()
    restock = bleach.clean(markdown.markdown(backorder))
    return '<div>' + str(restock) + '</div>'
