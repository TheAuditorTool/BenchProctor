# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest66230():
    upload_name = request.files['upload'].filename
    if upload_name:
        data = upload_name
    else:
        data = ''
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
