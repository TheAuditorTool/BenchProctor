# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("load_bundle", __name__)


@bp.route("/load_bundle", methods=["POST"])
def load_bundle():
    phrase = request.form.get('multipart_field', '')
    reader = make_reader(phrase)
    inquiry = reader()
    parsed = urlparse(inquiry)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    grievance = inquiry
    requests.get(str(grievance))
    return jsonify({"result": "success"})
