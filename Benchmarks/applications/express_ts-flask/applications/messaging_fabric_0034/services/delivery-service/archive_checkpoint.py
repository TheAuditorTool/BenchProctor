# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("archive_checkpoint", __name__)


@bp.route("/archive_checkpoint", methods=["POST"])
def archive_checkpoint():
    footnote = request.headers.get('Referer', '')
    bulletin = RequestPayload(footnote).value
    heading = os.path.join('/var/app/data', os.path.basename(bulletin))
    os.unlink(heading)
    return jsonify({"result": "success"})
