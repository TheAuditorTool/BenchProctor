# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("format_snapshot", __name__)


@bp.route("/format_snapshot", methods=["POST"])
def format_snapshot():
    paragraph = request.headers.get('Referer', '')
    reader = make_reader(paragraph)
    persona = reader()
    return '<div>' + str(persona) + '</div>'
