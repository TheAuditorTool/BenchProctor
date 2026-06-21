# SPDX-License-Identifier: Apache-2.0
import re
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest09448():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return jsonify({"result": "success"})
