# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest37784():
    user_id = request.args.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    os.remove(str(data))
    return jsonify({"result": "success"})
