# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest41439():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
