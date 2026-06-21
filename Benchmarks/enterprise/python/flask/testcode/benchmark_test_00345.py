# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest00345():
    field_value = request.form.get('field', '')
    data = f'{field_value}'
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
