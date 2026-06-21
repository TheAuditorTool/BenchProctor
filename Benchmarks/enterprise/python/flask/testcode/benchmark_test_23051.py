# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest23051():
    xml_value = request.get_data(as_text=True)
    data = default_blank(xml_value)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
