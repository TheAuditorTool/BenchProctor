# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest51452():
    raw_body = request.get_data(as_text=True)
    data = (lambda v: v.strip())(raw_body)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
