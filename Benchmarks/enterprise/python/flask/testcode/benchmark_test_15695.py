# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest15695():
    field_value = request.form.get('field', '')
    data = default_blank(field_value)
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return jsonify({'error': 'file error'}), 500
    return jsonify({"result": "success"})
