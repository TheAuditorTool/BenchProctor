# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest05066():
    raw_body = request.get_data(as_text=True)
    data = (lambda v: v.strip())(raw_body)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
