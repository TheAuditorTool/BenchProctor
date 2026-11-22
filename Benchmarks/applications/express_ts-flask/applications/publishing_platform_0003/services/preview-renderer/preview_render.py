# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from pathlib import Path


bp = Blueprint("render_preview", __name__)


@bp.route("/render_preview", methods=["POST"])
def render_preview():
    snippet = (request.get_json(silent=True) or {}).get("publishing_payload", "")
    allowed = {'config.json', 'index.html', 'readme.md'}
    if snippet not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    byline = '/var/app/data/' + snippet
    Path(byline).write_text('data')
    return jsonify({"result": "success"})
