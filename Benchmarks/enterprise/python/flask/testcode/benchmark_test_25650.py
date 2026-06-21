# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25650():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
