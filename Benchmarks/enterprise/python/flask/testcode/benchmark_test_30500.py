# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30500():
    multipart_value = request.form.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
