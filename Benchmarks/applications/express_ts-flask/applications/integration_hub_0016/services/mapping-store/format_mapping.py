# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("format_mapping", __name__)


@bp.route("/format_mapping", methods=["POST"])
def format_mapping():
    wording = request.headers.get('Referer', '')
    reader = make_reader(wording)
    handshake = reader()
    return '<div>' + str(handshake) + '</div>'
