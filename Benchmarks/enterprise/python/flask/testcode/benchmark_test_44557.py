# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest44557():
    field_value = request.form.get('field', '')
    parts = str(field_value).split(',')
    data = ','.join(parts)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
