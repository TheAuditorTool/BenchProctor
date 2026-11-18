# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("merge_policy", __name__)


@bp.route("/merge_policy", methods=["POST"])
def merge_policy():
    excerpt = request.form.get('multipart_field', '')
    reader = make_reader(excerpt)
    handshake = reader()
    parsed = urlparse(handshake)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    persona = handshake
    requests.get(str(persona))
    return jsonify({"result": "success"})
