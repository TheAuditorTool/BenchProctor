# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify


def BenchmarkTest35165():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
