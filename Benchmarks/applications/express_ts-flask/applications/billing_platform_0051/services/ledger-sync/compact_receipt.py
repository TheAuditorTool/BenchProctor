# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("compact_receipt", __name__)


@bp.route("/compact_receipt", methods=["POST"])
def compact_receipt():
    synopsis = request.form.get('multipart_field', '')
    reader = make_reader(synopsis)
    arrears = reader()
    parsed = urlparse(arrears)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    dunning = arrears
    requests.get(str(dunning))
    return jsonify({"result": "success"})
