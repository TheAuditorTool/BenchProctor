# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify


def BenchmarkTest06067(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
