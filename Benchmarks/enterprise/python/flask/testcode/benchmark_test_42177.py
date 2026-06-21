# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest42177():
    cookie_value = request.cookies.get('session_token', '')
    reader = make_reader(cookie_value)
    data = reader()
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
