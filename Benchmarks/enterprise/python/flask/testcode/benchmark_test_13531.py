# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify


def BenchmarkTest13531(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
