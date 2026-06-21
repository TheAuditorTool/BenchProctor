# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest42806():
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})
