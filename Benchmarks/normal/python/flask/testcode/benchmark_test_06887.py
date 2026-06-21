# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06887():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % (ua_value,)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
