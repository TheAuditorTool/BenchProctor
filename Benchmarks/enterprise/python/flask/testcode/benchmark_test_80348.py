# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest80348(path_param):
    path_value = path_param
    data = to_text(path_value)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
