# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest70235():
    multipart_value = request.form.get('multipart_field', '')
    data = '{}'.format(multipart_value)
    eval(str(data))
    return jsonify({"result": "success"})
