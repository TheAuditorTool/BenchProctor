# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
from flask import Blueprint, jsonify
import socket
import urllib.parse
import re
from app_runtime import db


bp = Blueprint("export_report", __name__)


@bp.route("/export_report", methods=["POST"])
def export_report():
    summary = db.fetch_one('SELECT text FROM comments LIMIT 1')
    phrase = summary if summary else 'default'
    parsed = urlparse(phrase)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", phrase) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    subtitle = phrase
    s = socket.create_connection((urllib.parse.urlparse(str(subtitle)).hostname, 80))
    s.close()
    return jsonify({"result": "success"})
