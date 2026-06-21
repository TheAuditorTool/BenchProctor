# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest63619():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
