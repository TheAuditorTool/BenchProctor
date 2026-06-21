# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify
import socket
from app_runtime import db


def BenchmarkTest27519():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
