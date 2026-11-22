# SPDX-License-Identifier: Apache-2.0
import urllib.request
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("prune_report", __name__)


@bp.route("/prune_report", methods=["POST"])
def prune_report():
    remark = db.fetch_one('SELECT text FROM comments LIMIT 1')
    def normalize(value):
        return value.strip()
    note = normalize(remark)
    outbound = urllib.request.Request(str(note), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
