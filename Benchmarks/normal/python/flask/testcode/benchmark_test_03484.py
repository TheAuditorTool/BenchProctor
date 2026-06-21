# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest03484():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
