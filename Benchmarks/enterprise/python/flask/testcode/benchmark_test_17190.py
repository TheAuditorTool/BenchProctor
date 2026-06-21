# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest17190():
    raw_body = request.get_data(as_text=True)
    data = normalise_input(raw_body)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
