# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest58667():
    multipart_value = request.form.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
