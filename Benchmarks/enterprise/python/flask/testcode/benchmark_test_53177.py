# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53177():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
