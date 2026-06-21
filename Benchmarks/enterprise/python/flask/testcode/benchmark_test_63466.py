# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
from flask import jsonify
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest63466():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
