# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest05808():
    origin_value = request.headers.get('Origin', '')
    data = normalise_input(origin_value)
    if os.environ.get("APP_ENV", "production") != "test":
        os.unlink('/var/app/data/' + str(data))
    return jsonify({"result": "success"})
