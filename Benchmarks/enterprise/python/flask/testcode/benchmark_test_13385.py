# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest13385():
    field_value = request.form.get('field', '')
    reader = make_reader(field_value)
    data = reader()
    auth_check('user', data)
    return jsonify({"result": "success"})
