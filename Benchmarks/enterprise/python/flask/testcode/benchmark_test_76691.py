# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import ctypes
from app_runtime import db


def BenchmarkTest76691():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(comment_value).split(',')
    data = ','.join(parts)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
