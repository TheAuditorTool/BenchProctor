# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest06342():
    origin_value = request.headers.get('Origin', '')
    data = normalise_input(origin_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
