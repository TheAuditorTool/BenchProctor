# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30681():
    upload_name = request.files['upload'].filename
    data = '%s' % (upload_name,)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
