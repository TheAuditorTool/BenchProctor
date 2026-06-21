# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75087():
    upload_name = request.files['upload'].filename
    data = '{}'.format(upload_name)
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
