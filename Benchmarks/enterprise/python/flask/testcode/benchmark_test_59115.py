# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest59115():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})
