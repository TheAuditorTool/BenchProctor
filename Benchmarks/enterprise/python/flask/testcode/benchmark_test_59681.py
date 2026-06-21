# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest59681():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = FormData(payload=forwarded_ip).payload
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return jsonify({"result": "success"})
