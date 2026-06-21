# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
from app_runtime import auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest02961():
    field_value = request.form.get('field', '')
    reader = make_reader(field_value)
    data = reader()
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return jsonify({"result": "success"})
