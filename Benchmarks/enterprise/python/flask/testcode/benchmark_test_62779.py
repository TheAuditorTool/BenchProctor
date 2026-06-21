# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify


def BenchmarkTest62779(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
