# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest54711():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % str(referer_value)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
