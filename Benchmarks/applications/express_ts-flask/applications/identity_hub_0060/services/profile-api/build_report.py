# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
from flask import Blueprint, jsonify
import socket
import urllib.parse
import re
from app_runtime import db


bp = Blueprint("build_report", __name__)


@bp.route("/build_report", methods=["POST"])
def build_report():
    paragraph = db.fetch_one('SELECT text FROM comments LIMIT 1')
    persona = paragraph if paragraph else 'default'
    parsed = urlparse(persona)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", persona) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    blurb = persona
    s = socket.create_connection((urllib.parse.urlparse(str(blurb)).hostname, 80))
    s.close()
    return jsonify({"result": "success"})
