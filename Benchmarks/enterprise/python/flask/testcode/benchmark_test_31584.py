# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31584():
    multipart_value = request.form.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
