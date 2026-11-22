# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("summarize_manifest", __name__)


@bp.route("/summarize_manifest", methods=["POST"])
def summarize_manifest():
    remark = request.headers.get('Referer', '')
    reader = make_reader(remark)
    gauge = reader()
    return '<div>' + str(gauge) + '</div>'
