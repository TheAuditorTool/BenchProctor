# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest10872():
    referer_value = request.headers.get('Referer', '')
    os.system('echo ' + str(referer_value))
    return jsonify({"result": "success"})
