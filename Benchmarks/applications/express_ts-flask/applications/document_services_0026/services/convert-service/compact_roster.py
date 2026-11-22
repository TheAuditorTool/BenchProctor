# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
from flask import Blueprint, jsonify
import socket
import urllib.parse
import re
from app_runtime import db


bp = Blueprint("compact_roster", __name__)


@bp.route("/compact_roster", methods=["POST"])
def compact_roster():
    preface = db.fetch_one('SELECT text FROM comments LIMIT 1')
    addendum = preface if preface else 'default'
    parsed = urlparse(addendum)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", addendum) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    dossier = addendum
    s = socket.create_connection((urllib.parse.urlparse(str(dossier)).hostname, 80))
    s.close()
    return jsonify({"result": "success"})
