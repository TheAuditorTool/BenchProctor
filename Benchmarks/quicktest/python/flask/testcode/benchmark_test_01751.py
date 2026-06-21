# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01751():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    eval(str(data))
    return jsonify({"result": "success"})
