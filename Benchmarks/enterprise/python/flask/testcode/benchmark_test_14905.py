# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14905():
    xml_value = request.get_data(as_text=True)
    data = '%s' % (xml_value,)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
