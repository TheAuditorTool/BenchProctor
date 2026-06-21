# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest08720():
    field_value = request.form.get('field', '')
    globals()['counter'] = int(field_value)
    return jsonify({"result": "success"})
