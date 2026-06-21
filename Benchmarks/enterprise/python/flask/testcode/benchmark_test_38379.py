# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest38379():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
