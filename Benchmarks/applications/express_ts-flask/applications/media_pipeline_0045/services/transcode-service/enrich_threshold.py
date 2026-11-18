# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("enrich_threshold", __name__)


@bp.route("/enrich_threshold", methods=["POST"])
def enrich_threshold():
    notice = request.headers.get('Referer', '')
    rendition = RequestPayload(notice).value
    with open('/var/app/data/' + str(rendition), 'r') as fh:
        content = fh.read()
    return content
