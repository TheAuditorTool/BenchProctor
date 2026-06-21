# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest39428():
    referer_value = request.headers.get('Referer', '')
    with open('/var/uploads/' + str(referer_value), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
