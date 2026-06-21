# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28173():
    referer_value = request.headers.get('Referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
