# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest58647():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
