# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest05163():
    referer_value = request.headers.get('Referer', '')
    try:
        os.setuid(int(str(referer_value)) if str(referer_value).isdigit() else 65534)
    except OSError:
        return jsonify({'error': 'privilege drop failed'}), 500
    return jsonify({"result": "success"})
