# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60192():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % (referer_value,)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
