# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest66365():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
