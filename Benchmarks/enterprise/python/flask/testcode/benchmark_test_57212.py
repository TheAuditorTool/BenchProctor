# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
import ctypes
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest57212():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
