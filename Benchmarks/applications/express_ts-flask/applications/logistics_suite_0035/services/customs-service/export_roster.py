# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("export_roster", __name__)


@bp.route("/export_roster", methods=["POST"])
def export_roster():
    phrase = request.form.get('multipart_field', '')
    reader = make_reader(phrase)
    parcel = reader()
    parsed = urlparse(parcel)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    consignment = parcel
    requests.get(str(consignment))
    return jsonify({"result": "success"})
