# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify


def BenchmarkTest37909(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
