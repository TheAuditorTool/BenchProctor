# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest42720():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = normalise_input(forwarded_ip)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
