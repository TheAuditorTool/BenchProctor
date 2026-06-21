# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import subprocess
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest74869():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
