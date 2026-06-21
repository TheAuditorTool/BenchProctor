# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest23486():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    os.remove(str(data))
    return jsonify({"result": "success"})
