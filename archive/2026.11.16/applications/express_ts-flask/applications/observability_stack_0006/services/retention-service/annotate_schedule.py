# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
import socket
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("annotate_schedule", __name__)


@bp.route("/annotate_schedule", methods=["POST"])
def annotate_schedule():
    preface = request.headers.get('X-Forwarded-For', '')
    cohort = f'{preface!s}'
    parsed = urlparse(cohort)
    resolved = socket.gethostbyname(parsed.hostname or cohort)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return jsonify({'error': 'private range blocked'}), 403
    gauge = cohort
    requests.get(str(gauge))
    return jsonify({"result": "success"})
