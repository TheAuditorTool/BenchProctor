# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest39036():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    request_state['last_input'] = profile_value
    data = request_state['last_input']
    processed = data[:64]
    with open('/var/app/data/' + str(processed), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
