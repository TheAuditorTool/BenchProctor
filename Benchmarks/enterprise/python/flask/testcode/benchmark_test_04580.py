# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest04580():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
