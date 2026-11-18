# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("verify_index", __name__)


@bp.route("/verify_index", methods=["POST"])
def verify_index():
    caption = request.form.get('multipart_field', '')
    reader = make_reader(caption)
    gauge = reader()
    parsed = urlparse(gauge)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    cohort = gauge
    requests.get(str(cohort))
    return jsonify({"result": "success"})
