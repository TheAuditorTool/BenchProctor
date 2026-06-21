# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import jsonify
import subprocess
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest18679():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
