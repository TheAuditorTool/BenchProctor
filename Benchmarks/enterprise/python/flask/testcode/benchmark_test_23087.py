# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest23087():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value:.200s}'
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return jsonify({"result": "success"})
