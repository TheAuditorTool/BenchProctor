# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import ctypes
from app_runtime import db


def BenchmarkTest69354():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = comment_value if comment_value else 'default'
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
