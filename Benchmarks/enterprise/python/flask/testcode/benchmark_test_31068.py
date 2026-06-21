# SPDX-License-Identifier: Apache-2.0
import threading
from dataclasses import dataclass
from flask import jsonify
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest31068():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
