# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify


def BenchmarkTest33088(path_param):
    path_value = path_param
    digest = hashlib.md5(str(path_value).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
