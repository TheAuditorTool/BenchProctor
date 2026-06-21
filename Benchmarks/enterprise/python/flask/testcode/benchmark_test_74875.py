# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def BenchmarkTest74875():
    ua_value = request.headers.get('User-Agent', '')
    data = ' '.join(str(ua_value).split())
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
