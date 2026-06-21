# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest43062():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    int(str(data))
    return jsonify({"result": "success"})
