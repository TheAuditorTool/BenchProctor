# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("load_header", __name__)


@bp.route("/load_header", methods=["POST"])
def load_header():
    passage = request.get_data(as_text=True)
    reader = make_reader(passage)
    persona = reader()
    return '<div>' + str(persona) + '</div>'
