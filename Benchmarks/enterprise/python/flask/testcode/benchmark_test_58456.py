# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest58456():
    xml_value = request.get_data(as_text=True)
    if xml_value:
        data = xml_value
    else:
        data = ''
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
