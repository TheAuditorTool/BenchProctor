# SPDX-License-Identifier: Apache-2.0
import hashlib
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest24700():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
