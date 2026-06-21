# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import time
import ast


def BenchmarkTest78810():
    referer_value = request.headers.get('Referer', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    if time.time() > 1000000000:
        os.unlink('/var/app/data/' + str(data))
    return jsonify({"result": "success"})
