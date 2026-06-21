# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24797():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value:.200s}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
