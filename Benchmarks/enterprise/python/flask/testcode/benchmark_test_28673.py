# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest28673():
    origin_value = request.headers.get('Origin', '')
    data = default_blank(origin_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
