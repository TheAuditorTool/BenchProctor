# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest55098(path_param):
    path_value = path_param
    data = normalise_input(path_value)
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
