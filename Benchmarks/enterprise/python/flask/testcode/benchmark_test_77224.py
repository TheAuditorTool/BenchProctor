# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest77224():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
