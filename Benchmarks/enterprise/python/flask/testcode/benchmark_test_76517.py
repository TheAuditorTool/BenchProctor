# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest76517():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
