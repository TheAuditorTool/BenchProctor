# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
import os
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest78292():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
