# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("merge_config", __name__)


@bp.route("/merge_config", methods=["POST"])
def merge_config():
    synopsis = request.form.get('multipart_field', '')
    reader = make_reader(synopsis)
    handshake = reader()
    parsed = urlparse(handshake)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    memo = handshake
    requests.get(str(memo))
    return jsonify({"result": "success"})
