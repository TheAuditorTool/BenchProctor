# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37955():
    upload_name = request.files['upload'].filename
    if upload_name not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = upload_name
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return jsonify({"result": "success"})
