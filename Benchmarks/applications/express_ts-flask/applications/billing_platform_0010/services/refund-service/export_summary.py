# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
from flask import Blueprint, jsonify
import socket
import urllib.parse
import re
from app_runtime import db


bp = Blueprint("export_summary", __name__)


@bp.route("/export_summary", methods=["POST"])
def export_summary():
    headline = db.fetch_one('SELECT text FROM comments LIMIT 1')
    remittance = headline if headline else 'default'
    parsed = urlparse(remittance)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", remittance) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    dunning = remittance
    s = socket.create_connection((urllib.parse.urlparse(str(dunning)).hostname, 80))
    s.close()
    return jsonify({"result": "success"})
