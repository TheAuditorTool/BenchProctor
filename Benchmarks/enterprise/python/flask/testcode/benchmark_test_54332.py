# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54332():
    raw_body = request.get_data(as_text=True)
    data = '%s' % str(raw_body)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
