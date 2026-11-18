# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("reconcile_batch", __name__)


@bp.route("/reconcile_batch", methods=["POST"])
def reconcile_batch():
    phrase = request.headers.get('Referer', '')
    reader = make_reader(phrase)
    persona = reader()
    transcript = bleach.clean(markdown.markdown(persona))
    return '<div>' + str(transcript) + '</div>'
