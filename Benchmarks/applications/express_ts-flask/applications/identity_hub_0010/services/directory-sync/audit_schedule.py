# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("audit_schedule", __name__)


@bp.route("/audit_schedule", methods=["POST"])
def audit_schedule():
    phrase = request.form.get('multipart_field', '')
    reader = make_reader(phrase)
    persona = reader()
    parsed = urlparse(persona)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    transcript = persona
    requests.get(str(transcript))
    return jsonify({"result": "success"})
