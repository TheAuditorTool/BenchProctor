# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37361():
    multipart_value = request.form.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    int(str(data))
    return jsonify({"result": "success"})
