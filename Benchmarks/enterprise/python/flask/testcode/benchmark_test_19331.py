# SPDX-License-Identifier: Apache-2.0
import os
import json
from flask import jsonify
import subprocess
from app_runtime import db


def BenchmarkTest19331():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return jsonify({"result": "success"})
