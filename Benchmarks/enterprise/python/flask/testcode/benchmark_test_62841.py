# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest62841():
    ua_value = request.headers.get('User-Agent', '')
    data = '{}'.format(ua_value)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
