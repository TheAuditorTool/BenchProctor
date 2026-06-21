# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49976():
    xml_value = request.get_data(as_text=True)
    data = xml_value.decode('utf-8', 'ignore') if isinstance(xml_value, bytes) else xml_value
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
