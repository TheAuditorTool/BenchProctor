# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest66495():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
