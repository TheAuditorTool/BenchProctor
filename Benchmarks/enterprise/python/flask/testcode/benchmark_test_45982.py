# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest45982():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
