# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import jsonify
import subprocess
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest52606():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return jsonify({"result": "success"})
