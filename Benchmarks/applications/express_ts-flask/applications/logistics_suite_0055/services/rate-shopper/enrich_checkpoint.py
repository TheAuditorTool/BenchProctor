# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("enrich_checkpoint", __name__)


@bp.route("/enrich_checkpoint", methods=["POST"])
def enrich_checkpoint():
    heading = request.get_data(as_text=True)
    reader = make_reader(heading)
    consignment = reader()
    return '<div>' + str(consignment) + '</div>'
