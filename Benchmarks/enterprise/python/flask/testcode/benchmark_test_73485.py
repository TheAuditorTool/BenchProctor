# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest73485():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
