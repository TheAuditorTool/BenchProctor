# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify


def BenchmarkTest63275(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
