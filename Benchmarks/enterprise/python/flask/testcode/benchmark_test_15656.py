# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest15656():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value}'
    os.unlink('/var/app/data/' + str(data))
    return jsonify({"result": "success"})
