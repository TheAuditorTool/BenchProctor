# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest15146():
    cookie_value = request.cookies.get('session_token', '')
    subprocess.run([str(cookie_value), '--status'], shell=False)
    return jsonify({"result": "success"})
