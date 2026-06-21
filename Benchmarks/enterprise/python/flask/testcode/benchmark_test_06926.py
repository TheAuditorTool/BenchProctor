# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06926():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
