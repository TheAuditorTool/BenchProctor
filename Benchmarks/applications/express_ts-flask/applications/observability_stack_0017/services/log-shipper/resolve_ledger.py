# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("resolve_ledger", __name__)


@bp.route("/resolve_ledger", methods=["POST"])
def resolve_ledger():
    note = request.headers.get('Referer', '')
    reader = make_reader(note)
    cohort = reader()
    return '<div>' + str(cohort) + '</div>'
