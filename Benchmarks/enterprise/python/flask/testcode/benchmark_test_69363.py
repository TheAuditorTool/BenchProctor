# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest69363():
    field_value = request.form.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
