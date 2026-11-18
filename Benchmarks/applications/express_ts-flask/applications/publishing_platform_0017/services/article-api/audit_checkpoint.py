# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("audit_checkpoint", __name__)


@bp.route("/audit_checkpoint", methods=["POST"])
def audit_checkpoint():
    summary = request.get_data(as_text=True)
    reader = make_reader(summary)
    addendum = reader()
    return '<div>' + str(addendum) + '</div>'
