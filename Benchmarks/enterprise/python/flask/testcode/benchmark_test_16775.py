# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16775():
    upload_name = request.files['upload'].filename
    data = '%s' % str(upload_name)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    exec(str(processed))
    return jsonify({"result": "success"})
