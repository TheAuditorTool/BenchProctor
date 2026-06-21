# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest47383():
    ua_value = request.headers.get('User-Agent', '')
    data = coalesce_blank(ua_value)
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
