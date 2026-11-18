# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("format_bundle", __name__)


@bp.route("/format_bundle", methods=["POST"])
def format_bundle():
    headline = request.form.get('multipart_field', '')
    reader = make_reader(headline)
    cohort = reader()
    parsed = urlparse(cohort)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    gauge = cohort
    requests.get(str(gauge))
    return jsonify({"result": "success"})
