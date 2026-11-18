# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("render_window", __name__)


@bp.route("/render_window", methods=["POST"])
def render_window():
    synopsis = request.get_data(as_text=True)
    reader = make_reader(synopsis)
    handshake = reader()
    return '<div>' + str(handshake) + '</div>'
