# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest60533():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
