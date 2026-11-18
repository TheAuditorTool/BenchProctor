# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("prune_checkpoint", __name__)


@bp.route("/prune_checkpoint", methods=["POST"])
def prune_checkpoint():
    note = request.headers.get('Referer', '')
    gauge = RequestPayload(note).value
    cohort = os.path.join('/var/app/data', os.path.basename(gauge))
    os.unlink(cohort)
    return jsonify({"result": "success"})
