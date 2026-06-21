# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
from flask import jsonify
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest64553():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    requests.get(str(data))
    return jsonify({"result": "success"})
