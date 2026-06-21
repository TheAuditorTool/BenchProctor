# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify
import json


def BenchmarkTest80036():
    user_id = request.args.get('id', '')
    try:
        data = json.loads(user_id).get('value', user_id)
    except (json.JSONDecodeError, AttributeError):
        data = user_id
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
