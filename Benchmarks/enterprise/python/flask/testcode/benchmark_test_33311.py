# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
import defusedxml.ElementTree
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest33311():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
