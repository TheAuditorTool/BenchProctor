# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("verify_receipt", __name__)


@bp.route("/verify_receipt", methods=["POST"])
def verify_receipt():
    wording = request.form.get('multipart_field', '')
    reader = make_reader(wording)
    remark = reader()
    parsed = urlparse(remark)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    phrase = remark
    requests.get(str(phrase))
    return jsonify({"result": "success"})
