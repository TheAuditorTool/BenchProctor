# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest29924():
    upload_name = request.files['upload'].filename
    prefix = ''
    data = prefix + str(upload_name)
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
