# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16357():
    multipart_value = request.form.get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ','.join(parts)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
