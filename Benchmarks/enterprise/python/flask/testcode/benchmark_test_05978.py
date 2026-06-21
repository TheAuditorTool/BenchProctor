# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest05978():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
