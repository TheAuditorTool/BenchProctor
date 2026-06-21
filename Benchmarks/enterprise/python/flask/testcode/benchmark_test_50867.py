# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest50867():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    os.remove(str(data))
    return jsonify({"result": "success"})
