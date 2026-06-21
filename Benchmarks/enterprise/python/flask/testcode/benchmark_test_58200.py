# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest58200():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = normalise_input(forwarded_ip)
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
