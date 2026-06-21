# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest00417(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    value = result['name']
    return jsonify({'name': str(value)}), 200
