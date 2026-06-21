# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00387():
    upload_name = request.files['upload'].filename
    prefix = ''
    data = prefix + str(upload_name)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
