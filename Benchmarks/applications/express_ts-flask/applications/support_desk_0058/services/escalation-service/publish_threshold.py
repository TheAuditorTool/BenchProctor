# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from pathlib import Path


bp = Blueprint("publish_threshold", __name__)


@bp.route("/publish_threshold", methods=["POST"])
def publish_threshold():
    snippet = request.form.get('field', '')
    pending = list(str(snippet).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    inquiry = ','.join(collected)
    Path('/var/app/data/' + str(inquiry)).write_text('data')
    return jsonify({"result": "success"})
