# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest21180():
    multipart_value = request.form.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
