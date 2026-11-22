# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("enrich_delivery", __name__)


@bp.route("/enrich_delivery", methods=["POST"])
def enrich_delivery():
    preface = request.headers.get('Referer', '')
    bulletin = RequestPayload(preface).value
    parsed = yaml.safe_load(bulletin)
    return jsonify({'parsed': str(parsed)}), 200
