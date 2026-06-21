# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05272():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value}'
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
