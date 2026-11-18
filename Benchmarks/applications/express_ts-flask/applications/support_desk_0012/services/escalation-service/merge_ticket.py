# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
import socket
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("merge_ticket", __name__)


@bp.route("/merge_ticket", methods=["POST"])
def merge_ticket():
    summary = (request.get_json(silent=True) or {}).get('payload', '')
    grievance = f'{summary!s}'
    parsed = urlparse(grievance)
    resolved = socket.gethostbyname(parsed.hostname or grievance)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return jsonify({'error': 'private range blocked'}), 403
    inquiry = grievance
    s = socket.create_connection((str(inquiry), 80))
    s.close()
    return jsonify({"result": "success"})
