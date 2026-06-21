# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest64282():
    raw_body = request.get_data(as_text=True)
    data = relay_value(raw_body)
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        return jsonify({'error': 'privilege drop failed'}), 500
    return jsonify({"result": "success"})
