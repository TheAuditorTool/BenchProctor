# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("reconcile_batch", __name__)


@bp.route("/reconcile_batch", methods=["POST"])
def reconcile_batch():
    summary = request.headers.get('Referer', '')
    grievance = RequestPayload(summary).value
    verdict = os.path.join('/var/app/data', os.path.basename(grievance))
    os.unlink(verdict)
    return jsonify({"result": "success"})
