# SPDX-License-Identifier: Apache-2.0
import hashlib
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest70333(path_param):
    path_value = path_param
    data = unquote(path_value)
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
