# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest65856():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})
