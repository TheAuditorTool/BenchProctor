# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest80943():
    upload_name = request.files['upload'].filename
    data = '{}'.format(upload_name)
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
