# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest46566():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    try:
        processed = int(data)
    except (TypeError, ValueError):
        return jsonify({'error': 'forbidden'}), 400
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return jsonify({"result": "success"})
