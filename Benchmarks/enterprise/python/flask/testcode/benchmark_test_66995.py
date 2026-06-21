# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest66995():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    eval(str(data))
    return jsonify({"result": "success"})
