# SPDX-License-Identifier: Apache-2.0
import os
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest41536():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
