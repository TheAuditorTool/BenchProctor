# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("archive_manifest", __name__)


@bp.route("/archive_manifest", methods=["POST"])
def archive_manifest():
    excerpt = request.get_data(as_text=True)
    cohort = (lambda v: v.strip())(excerpt)
    parsed = json.loads(cohort)
    return jsonify({'parsed': str(parsed)}), 200
