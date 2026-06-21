# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64836():
    ua_value = request.headers.get('User-Agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
