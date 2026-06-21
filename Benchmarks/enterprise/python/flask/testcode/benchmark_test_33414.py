# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
import socket
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest33414():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    s = socket.create_connection((str(data), 80))
    s.close()
    return jsonify({"result": "success"})
