# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest29772():
    raw_body = request.get_data(as_text=True)
    data = (lambda v: v.strip())(raw_body)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
