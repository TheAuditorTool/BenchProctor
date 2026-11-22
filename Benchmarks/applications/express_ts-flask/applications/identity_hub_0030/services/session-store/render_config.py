# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("render_config", __name__)


@bp.route("/render_config", methods=["POST"])
def render_config():
    tagline = (request.get_json(silent=True) or {}).get('payload', '')
    reader = make_reader(tagline)
    persona = reader()
    with open('/var/app/data/' + str(persona), 'r') as fh:
        content = fh.read()
    return content
