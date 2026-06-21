# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest70868():
    xml_value = request.get_data(as_text=True)
    data = (lambda v: v.strip())(xml_value)
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
