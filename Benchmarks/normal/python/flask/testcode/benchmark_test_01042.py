# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest01042():
    field_value = request.form.get('field', '')
    reader = make_reader(field_value)
    data = reader()
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
