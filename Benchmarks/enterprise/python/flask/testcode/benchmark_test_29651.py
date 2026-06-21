# SPDX-License-Identifier: Apache-2.0
import os
from pathlib import Path
from flask import jsonify
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest29651():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = str(candidate)
    os.unlink(checked_path)
    return jsonify({"result": "success"})
