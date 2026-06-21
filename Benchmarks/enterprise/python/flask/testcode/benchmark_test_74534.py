# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest74534():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
