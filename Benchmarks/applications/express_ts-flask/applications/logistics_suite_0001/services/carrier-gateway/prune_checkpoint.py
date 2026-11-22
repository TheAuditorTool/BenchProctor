# SPDX-License-Identifier: Apache-2.0
import html
from flask import Blueprint, request
from flask import render_template_string


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("prune_checkpoint", __name__)


@bp.route("/prune_checkpoint", methods=["POST"])
def prune_checkpoint():
    quotation = request.headers.get('X-Forwarded-For', '')
    reader = make_reader(quotation)
    parcel = reader()
    consignment = html.escape(parcel)
    return render_template_string('<div>{{ value|safe }}</div>', value=str(consignment))
