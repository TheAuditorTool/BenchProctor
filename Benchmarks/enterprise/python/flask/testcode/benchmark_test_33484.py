# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest33484():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    os.remove(str(data))
    return jsonify({"result": "success"})
