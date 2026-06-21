# SPDX-License-Identifier: Apache-2.0
import re
import os
from flask import jsonify
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest07249():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return jsonify({"result": "success"})
