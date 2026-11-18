# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("export_bundle", __name__)


@bp.route("/export_bundle", methods=["POST"])
def export_bundle():
    subject = request.headers.get('Referer', '')
    bulletin = RequestPayload(subject).value
    with open('/var/app/data/' + str(bulletin), 'r') as fh:
        content = fh.read()
    return content
