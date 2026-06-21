# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest02666():
    referer_value = request.headers.get('Referer', '')
    data = to_text(referer_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
