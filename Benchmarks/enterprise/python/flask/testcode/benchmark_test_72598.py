# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72598():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % (referer_value,)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
