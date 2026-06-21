# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import jsonify
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest26482():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
