# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("compact_revision", __name__)


@bp.route("/compact_revision", methods=["POST"])
def compact_revision():
    synopsis = request.form.get('multipart_field', '')
    reader = make_reader(synopsis)
    byline = reader()
    parsed = urlparse(byline)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    addendum = byline
    requests.get(str(addendum))
    return jsonify({"result": "success"})
