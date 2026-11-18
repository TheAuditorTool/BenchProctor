# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("build_decision", __name__)


@bp.route("/build_decision", methods=["POST"])
def build_decision():
    summary = request.headers.get('Referer', '')
    grievance = RequestPayload(summary).value
    verdict = os.path.join('/var/app/data', os.path.basename(grievance))
    os.unlink(verdict)
    return jsonify({"result": "success"})
