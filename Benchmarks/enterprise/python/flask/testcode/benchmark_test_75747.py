# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
import importlib
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest75747():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
