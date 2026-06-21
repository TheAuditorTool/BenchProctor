# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest03114():
    field_value = request.form.get('field', '')
    data = '%s' % str(field_value)
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
