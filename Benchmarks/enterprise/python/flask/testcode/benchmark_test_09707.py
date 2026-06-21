# SPDX-License-Identifier: Apache-2.0
import re
import os
from flask import jsonify
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest09707():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.{}\\[\\]:_$\'\\"|=-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    db.users.find({'$where': "this.username == '" + str(processed) + "'"})
    return jsonify({"result": "success"})
