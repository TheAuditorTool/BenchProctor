# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest57908():
    xml_value = request.get_data(as_text=True)
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(xml_value)
    data = collected
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
