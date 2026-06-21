# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify


def BenchmarkTest75692():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value:.200s}'
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return jsonify({"result": "success"})
