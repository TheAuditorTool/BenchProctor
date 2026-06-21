# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest45190():
    raw_body = request.get_data(as_text=True)
    if raw_body:
        data = raw_body
    else:
        data = ''
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
