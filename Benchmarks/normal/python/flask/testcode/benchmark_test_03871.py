# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest03871():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value:.200s}'
    os.seteuid(65534)
    return jsonify({"result": "success"})
