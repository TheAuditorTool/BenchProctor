# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest28848():
    multipart_value = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
