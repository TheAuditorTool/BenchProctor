# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("normalize_policy", __name__)


@bp.route("/normalize_policy", methods=["POST"])
def normalize_policy():
    caption = (request.get_json(silent=True) or {}).get('payload', '')
    reader = make_reader(caption)
    synopsis = reader()
    with open('/var/app/data/' + str(synopsis), 'r') as fh:
        content = fh.read()
    return content
