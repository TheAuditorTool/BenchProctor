# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
import ctypes
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest35033():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
