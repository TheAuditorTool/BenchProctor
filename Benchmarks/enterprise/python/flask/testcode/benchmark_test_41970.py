# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41970():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
