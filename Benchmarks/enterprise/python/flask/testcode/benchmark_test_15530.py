# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest15530():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % (referer_value,)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
