# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify


def BenchmarkTest63905():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % (ua_value,)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
