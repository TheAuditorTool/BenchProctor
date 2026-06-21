# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest09352():
    user_id = request.args.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
