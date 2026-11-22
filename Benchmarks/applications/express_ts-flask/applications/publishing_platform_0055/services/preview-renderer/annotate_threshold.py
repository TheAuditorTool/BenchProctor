# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("annotate_threshold", __name__)


@bp.route("/annotate_threshold", methods=["POST"])
def annotate_threshold():
    synopsis = request.headers.get('Referer', '')
    byline = RequestPayload(synopsis).value
    parsed = yaml.safe_load(byline)
    return jsonify({'parsed': str(parsed)}), 200
