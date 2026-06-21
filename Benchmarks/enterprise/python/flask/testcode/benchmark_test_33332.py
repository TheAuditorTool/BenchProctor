# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
import os
from flask import jsonify
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest33332():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})
