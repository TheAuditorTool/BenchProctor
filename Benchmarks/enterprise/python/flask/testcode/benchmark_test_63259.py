# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest63259():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
