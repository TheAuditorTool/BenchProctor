# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("enrich_threshold", __name__)


@bp.route("/enrich_threshold", methods=["POST"])
def enrich_threshold():
    synopsis = request.headers.get('Referer', '')
    byline = RequestPayload(synopsis).value
    addendum = os.path.join('/var/app/data', os.path.basename(byline))
    os.unlink(addendum)
    return jsonify({"result": "success"})
