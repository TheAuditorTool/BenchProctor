# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest78553():
    xml_value = request.get_data(as_text=True)
    data = ' '.join(str(xml_value).split())
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
