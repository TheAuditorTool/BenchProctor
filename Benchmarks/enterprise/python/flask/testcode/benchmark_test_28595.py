# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
import os


def BenchmarkTest28595(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
