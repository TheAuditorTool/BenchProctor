# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest07365():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
