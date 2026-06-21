# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify


def BenchmarkTest52004(path_param):
    path_value = path_param
    if path_value not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = path_value
    session['data'] = str(processed)
    return jsonify({"result": "success"})
