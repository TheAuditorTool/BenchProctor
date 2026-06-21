# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest70857():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
