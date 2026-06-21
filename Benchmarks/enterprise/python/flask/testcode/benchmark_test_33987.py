# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest33987():
    user_id = request.args.get('id', '')
    data = '%s' % str(user_id)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
