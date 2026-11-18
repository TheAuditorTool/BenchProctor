# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("enrich_receipt", __name__)


@bp.route("/enrich_receipt", methods=["POST"])
def enrich_receipt():
    paragraph = request.headers.get('Referer', '')
    reader = make_reader(paragraph)
    persona = reader()
    synopsis = bleach.clean(markdown.markdown(persona))
    return '<div>' + str(synopsis) + '</div>'
