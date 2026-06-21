# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import time


def relay_value(value):
    return value

def BenchmarkTest39964():
    user_id = request.args.get('id', '')
    data = relay_value(user_id)
    if time.time() > 1000000000:
        link_path = os.path.join('/var/app/data', str(data))
        target = os.readlink(link_path)
        with open(target, 'r') as fh:
            content = fh.read()
        return content
    return jsonify({"result": "success"})
