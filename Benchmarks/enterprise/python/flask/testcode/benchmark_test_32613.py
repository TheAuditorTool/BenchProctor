# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import jsonify
from app_runtime import db


def BenchmarkTest32613(path_param):
    path_value = path_param
    data = unquote(path_value)
    try:
        processed = int(data)
    except (TypeError, ValueError):
        return jsonify({'error': 'forbidden'}), 400
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return jsonify({"result": "success"})
