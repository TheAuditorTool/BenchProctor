# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest18102():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
