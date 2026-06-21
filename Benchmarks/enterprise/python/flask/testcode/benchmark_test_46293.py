# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest46293():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
