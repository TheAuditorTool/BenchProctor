# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09582():
    upload_name = request.files['upload'].filename
    globals().setdefault('_secret_cache', {})['current'] = str(upload_name)
    return jsonify({"result": "success"})
