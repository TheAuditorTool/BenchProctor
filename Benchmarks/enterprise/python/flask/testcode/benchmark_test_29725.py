# SPDX-License-Identifier: Apache-2.0
import os
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest29725():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        return jsonify({'error': 'privilege drop failed'}), 500
    return jsonify({"result": "success"})
