# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64977():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
