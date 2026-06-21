# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest73304():
    multipart_value = request.form.get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    eval(str(data))
    return jsonify({"result": "success"})
