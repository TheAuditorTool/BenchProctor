# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest71898():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
