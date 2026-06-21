# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest12655():
    referer_value = request.headers.get('Referer', '')
    data = (lambda v: v.strip())(referer_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
