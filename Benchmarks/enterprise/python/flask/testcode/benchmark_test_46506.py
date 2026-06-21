# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest46506():
    host_value = request.headers.get('Host', '')
    data = str(host_value).replace('\x00', '')
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
