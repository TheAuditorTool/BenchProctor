# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("merge_digest", __name__)


@bp.route("/merge_digest", methods=["POST"])
def merge_digest():
    footnote = request.headers.get('Referer', '')
    byline = RequestPayload(footnote).value
    addendum = os.path.join('/var/app/data', os.path.basename(byline))
    os.unlink(addendum)
    return jsonify({"result": "success"})
