# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import jsonify
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest02049():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    yaml.safe_load(data)
    return jsonify({"result": "success"})
