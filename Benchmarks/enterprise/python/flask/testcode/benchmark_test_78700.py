# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify


def BenchmarkTest78700():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
