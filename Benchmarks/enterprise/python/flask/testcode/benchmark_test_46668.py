# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest46668():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
