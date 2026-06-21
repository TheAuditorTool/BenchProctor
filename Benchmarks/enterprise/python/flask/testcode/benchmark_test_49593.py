# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest49593():
    xml_value = request.get_data(as_text=True)
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(xml_value)
    data = collected
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
