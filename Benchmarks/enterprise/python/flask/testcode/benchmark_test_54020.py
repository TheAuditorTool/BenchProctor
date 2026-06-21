# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest54020():
    host_value = request.headers.get('Host', '')
    prefix = ''
    data = prefix + str(host_value)
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
