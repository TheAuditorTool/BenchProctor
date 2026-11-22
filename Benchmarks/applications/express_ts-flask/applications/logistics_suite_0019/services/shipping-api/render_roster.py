# SPDX-License-Identifier: Apache-2.0
import urllib.request
from flask import Blueprint, request, jsonify


bp = Blueprint("render_roster", __name__)


@bp.route("/render_roster", methods=["POST"])
def render_roster():
    citation = request.headers.get('Authorization', '')
    parcel = f'{citation!s}'
    outbound = urllib.request.Request(str(parcel), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
