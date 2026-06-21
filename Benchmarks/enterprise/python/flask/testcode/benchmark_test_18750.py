# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest18750():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return jsonify({"result": "success"})
