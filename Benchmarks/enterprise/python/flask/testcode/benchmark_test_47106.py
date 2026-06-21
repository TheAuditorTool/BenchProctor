# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest47106():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value:.200s}'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
