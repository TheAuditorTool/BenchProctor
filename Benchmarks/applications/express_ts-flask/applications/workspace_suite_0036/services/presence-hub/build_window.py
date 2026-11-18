# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("build_window", __name__)


@bp.route("/build_window", methods=["POST"])
def build_window():
    remark = request.headers.get('Referer', '')
    synopsis = RequestPayload(remark).value
    quotation = os.path.join('/var/app/data', os.path.basename(synopsis))
    os.unlink(quotation)
    return jsonify({"result": "success"})
