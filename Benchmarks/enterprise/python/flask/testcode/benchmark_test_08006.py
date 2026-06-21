# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest08006():
    user_id = request.args.get('id', '')
    os.system('echo ' + str(user_id))
    return jsonify({"result": "success"})
