# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest12256():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
