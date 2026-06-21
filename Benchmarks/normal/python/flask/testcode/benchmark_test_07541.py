# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07541():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
