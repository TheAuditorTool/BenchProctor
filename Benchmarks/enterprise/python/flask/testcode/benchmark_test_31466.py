# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest31466():
    raw_body = request.get_data(as_text=True)
    reader = make_reader(raw_body)
    data = reader()
    auth_check('user', data)
    return jsonify({"result": "success"})
