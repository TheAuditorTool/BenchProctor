# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06249():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body:.200s}'
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
