# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest60012():
    multipart_value = request.form.get('multipart_field', '')
    data = '{}'.format(multipart_value)
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
