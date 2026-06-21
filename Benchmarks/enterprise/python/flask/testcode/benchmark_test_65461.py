# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest65461():
    env_value = os.environ.get('USER_INPUT', '')
    _resp = requests.get(str(env_value))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})
