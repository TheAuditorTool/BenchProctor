# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16892():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
