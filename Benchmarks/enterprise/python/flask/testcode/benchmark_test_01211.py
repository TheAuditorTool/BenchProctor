# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify


def BenchmarkTest01211(path_param):
    path_value = path_param
    digest = str(path_value).encode().hex()
    return jsonify({'digest': str(digest)}), 200
