# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest09295():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
