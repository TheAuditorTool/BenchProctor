# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
from flask import Blueprint, jsonify
import socket
import urllib.parse
import re
from app_runtime import db


bp = Blueprint("rotate_profile", __name__)


@bp.route("/rotate_profile", methods=["POST"])
def rotate_profile():
    excerpt = db.fetch_one('SELECT text FROM comments LIMIT 1')
    restock = excerpt if excerpt else 'default'
    parsed = urlparse(restock)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", restock) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    backorder = restock
    s = socket.create_connection((urllib.parse.urlparse(str(backorder)).hostname, 80))
    s.close()
    return jsonify({"result": "success"})
