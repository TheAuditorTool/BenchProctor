# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify


def BenchmarkTest25681():
    xml_value = request.get_data(as_text=True)
    if xml_value:
        data = xml_value
    else:
        data = ''
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
