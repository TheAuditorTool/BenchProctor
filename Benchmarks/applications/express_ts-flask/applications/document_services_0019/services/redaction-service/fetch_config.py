# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("fetch_config", __name__)


@bp.route("/fetch_config", methods=["POST"])
def fetch_config():
    passage = request.headers.get('Referer', '')
    dossier = RequestPayload(passage).value
    addendum = os.path.join('/var/app/data', os.path.basename(dossier))
    os.unlink(addendum)
    return jsonify({"result": "success"})
