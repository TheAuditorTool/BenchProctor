# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest25812():
    xml_value = request.get_data(as_text=True)
    digest = hashlib.sha256(str(xml_value).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
