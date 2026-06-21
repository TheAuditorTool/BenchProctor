# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest55976():
    upload_name = request.files['upload'].filename
    data = f'{upload_name}'
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
