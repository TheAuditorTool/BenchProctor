# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest47759():
    host_value = request.headers.get('Host', '')
    data = str(host_value).replace('\x00', '')
    os.remove(str(data))
    return jsonify({"result": "success"})
