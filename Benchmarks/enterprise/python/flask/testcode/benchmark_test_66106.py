# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest66106():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    int(str(data))
    return jsonify({"result": "success"})
