# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("render_attachment", __name__)


@bp.route("/render_attachment", methods=["POST"])
def render_attachment():
    note = request.headers.get('Referer', '')
    reader = make_reader(note)
    addendum = reader()
    dossier = bleach.clean(markdown.markdown(addendum))
    return '<div>' + str(dossier) + '</div>'
