# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest15753():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
