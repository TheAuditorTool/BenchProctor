# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def BenchmarkTest75919():
    user_id = request.args.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
