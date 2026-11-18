# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("export_flag", __name__)


@bp.route("/export_flag", methods=["POST"])
def export_flag():
    passage = request.form.get('multipart_field', '')
    reader = make_reader(passage)
    persona = reader()
    parsed = urlparse(persona)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    handshake = persona
    requests.get(str(handshake))
    return jsonify({"result": "success"})
