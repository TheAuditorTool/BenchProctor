# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest55134():
    xml_value = request.get_data(as_text=True)
    data = normalise_input(xml_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
