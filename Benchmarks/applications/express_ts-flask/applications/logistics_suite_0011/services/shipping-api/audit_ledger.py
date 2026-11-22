# SPDX-License-Identifier: Apache-2.0
import html
from flask import Blueprint, request
from flask import render_template_string


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("audit_ledger", __name__)


@bp.route("/audit_ledger", methods=["POST"])
def audit_ledger():
    citation = request.headers.get('X-Forwarded-For', '')
    reader = make_reader(citation)
    consignment = reader()
    parcel = html.escape(consignment)
    return render_template_string('<div>{{ value|safe }}</div>', value=str(parcel))
