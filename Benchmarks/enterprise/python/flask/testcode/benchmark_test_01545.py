# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01545():
    multipart_value = request.form.get('multipart_field', '')
    prefix = ''
    data = prefix + str(multipart_value)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
