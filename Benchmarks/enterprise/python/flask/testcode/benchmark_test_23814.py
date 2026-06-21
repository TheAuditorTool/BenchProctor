# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest23814():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
