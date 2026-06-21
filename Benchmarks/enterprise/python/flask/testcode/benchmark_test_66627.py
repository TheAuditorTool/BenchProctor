# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest66627():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
