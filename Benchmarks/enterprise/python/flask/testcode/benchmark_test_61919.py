# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest61919():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
