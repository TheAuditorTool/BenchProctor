# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest73112():
    user_id = request.args.get('id', '')
    data = f'{user_id}'
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
