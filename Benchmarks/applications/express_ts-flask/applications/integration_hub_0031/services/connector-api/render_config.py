# SPDX-License-Identifier: Apache-2.0
import base64
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("render_config", __name__)


@bp.route("/render_config", methods=["POST"])
def render_config():
    snippet = db.fetch_one('SELECT name FROM users LIMIT 1')
    handshake = base64.b64decode(snippet).decode('utf-8', 'ignore')
    try:
        _coerced = int(handshake)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    paragraph = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(paragraph))
    return jsonify({"result": "success"})
