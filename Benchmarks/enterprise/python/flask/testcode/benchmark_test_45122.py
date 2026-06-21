# SPDX-License-Identifier: Apache-2.0
import os
from urllib.parse import unquote
from flask import request, jsonify
import subprocess


def BenchmarkTest45122():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
