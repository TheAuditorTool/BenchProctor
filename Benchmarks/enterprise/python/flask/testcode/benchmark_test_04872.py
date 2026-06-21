# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04872():
    raw_body = request.get_data(as_text=True)
    data = '%s' % (raw_body,)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
