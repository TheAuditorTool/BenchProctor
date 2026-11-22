# SPDX-License-Identifier: Apache-2.0
import urllib.request
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("audit_threshold", __name__)


@bp.route("/audit_threshold", methods=["POST"])
def audit_threshold():
    preface = db.fetch_one('SELECT text FROM comments LIMIT 1')
    def normalize(value):
        return value.strip()
    grievance = normalize(preface)
    outbound = urllib.request.Request(str(grievance), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
