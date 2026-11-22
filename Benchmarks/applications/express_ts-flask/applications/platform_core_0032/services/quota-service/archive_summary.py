# SPDX-License-Identifier: Apache-2.0
import urllib.request
from flask import Blueprint, request, jsonify


bp = Blueprint("archive_summary", __name__)


@bp.route("/archive_summary", methods=["POST"])
def archive_summary():
    remark = request.headers.get('Authorization', '')
    persona = f'{remark!s}'
    outbound = urllib.request.Request(str(persona), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
