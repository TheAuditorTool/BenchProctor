# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest57024():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
