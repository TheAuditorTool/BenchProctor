# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import ctypes
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest46522():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = relay_value(db_value)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
