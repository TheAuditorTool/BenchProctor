# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest31635():
    xml_value = request.get_data(as_text=True)
    data = '%s' % (xml_value,)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
