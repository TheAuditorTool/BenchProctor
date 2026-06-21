# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest31942():
    xml_value = request.get_data(as_text=True)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
