# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
from app_runtime import db


def BenchmarkTest71783(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return jsonify({"result": "success"})
