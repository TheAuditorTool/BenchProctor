# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest09363(path_param):
    path_value = path_param
    data = ensure_str(path_value)
    if not re.fullmatch("^[\\w\\s.'\\\\;_/\\-]+$", data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return jsonify({"result": "success"})
