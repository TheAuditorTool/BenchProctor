# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import os
from flask import jsonify
import ctypes


@dataclass
class FormData:
    payload: str

def BenchmarkTest57777():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
