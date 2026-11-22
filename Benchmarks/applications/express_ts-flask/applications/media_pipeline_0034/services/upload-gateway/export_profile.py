# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
from flask import Blueprint, jsonify
import socket
import urllib.parse
import re
from app_runtime import db


bp = Blueprint("export_profile", __name__)


@bp.route("/export_profile", methods=["POST"])
def export_profile():
    synopsis = db.fetch_one('SELECT text FROM comments LIMIT 1')
    rendition = synopsis if synopsis else 'default'
    parsed = urlparse(rendition)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", rendition) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    montage = rendition
    s = socket.create_connection((urllib.parse.urlparse(str(montage)).hostname, 80))
    s.close()
    return jsonify({"result": "success"})
