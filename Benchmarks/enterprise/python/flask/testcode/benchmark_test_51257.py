# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest51257():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
