# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("reconcile_snapshot", __name__)


@bp.route("/reconcile_snapshot", methods=["POST"])
def reconcile_snapshot():
    caption = request.headers.get('Referer', '')
    reader = make_reader(caption)
    handshake = reader()
    return '<div>' + str(handshake) + '</div>'
