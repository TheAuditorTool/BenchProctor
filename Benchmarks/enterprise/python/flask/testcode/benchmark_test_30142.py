# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest30142():
    xml_value = request.get_data(as_text=True)
    data = (lambda v: v.strip())(xml_value)
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
