# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest77726():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
