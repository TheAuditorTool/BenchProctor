# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37023():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % (origin_value,)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
