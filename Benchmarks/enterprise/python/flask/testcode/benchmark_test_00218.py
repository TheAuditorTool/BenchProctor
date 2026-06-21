# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest00218():
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    eval(compile("_resp = requests.get(str(data))\ndb.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))", '<sink>', 'exec'))
    return jsonify({"result": "success"})
