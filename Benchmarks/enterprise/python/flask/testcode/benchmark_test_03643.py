# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest03643():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body:.200s}'
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
