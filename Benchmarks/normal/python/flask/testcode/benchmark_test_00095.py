# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest00095():
    xml_value = request.get_data(as_text=True)
    if not auth_check('user', hashlib.sha256(str(xml_value).encode()).hexdigest()):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
