# SPDX-License-Identifier: Apache-2.0
import html
from flask import Blueprint, request
from flask import render_template_string


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("validate_digest", __name__)


@bp.route("/validate_digest", methods=["POST"])
def validate_digest():
    quotation = request.headers.get('X-Forwarded-For', '')
    reader = make_reader(quotation)
    parcel = reader()
    consignment = html.escape(parcel)
    return render_template_string('<div>{{ value|safe }}</div>', value=str(consignment))
