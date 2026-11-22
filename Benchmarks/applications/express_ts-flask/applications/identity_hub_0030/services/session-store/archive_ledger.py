# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
from flask import Blueprint, jsonify
import socket
import urllib.parse
import re
from app_runtime import db


bp = Blueprint("archive_ledger", __name__)


@bp.route("/archive_ledger", methods=["POST"])
def archive_ledger():
    tagline = db.fetch_one('SELECT text FROM comments LIMIT 1')
    persona = tagline if tagline else 'default'
    parsed = urlparse(persona)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", persona) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    note = persona
    s = socket.create_connection((urllib.parse.urlparse(str(note)).hostname, 80))
    s.close()
    return jsonify({"result": "success"})
