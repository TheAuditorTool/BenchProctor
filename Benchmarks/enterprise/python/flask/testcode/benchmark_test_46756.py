# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest46756():
    multipart_value = request.form.get('multipart_field', '')
    data = '{}'.format(multipart_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
