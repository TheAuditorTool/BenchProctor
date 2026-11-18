# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("merge_threshold", __name__)


@bp.route("/merge_threshold", methods=["POST"])
def merge_threshold():
    summary = request.headers.get('Referer', '')
    reader = make_reader(summary)
    restock = reader()
    backorder = bleach.clean(markdown.markdown(restock))
    return '<div>' + str(backorder) + '</div>'
