# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest63190():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
