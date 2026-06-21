# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest12048():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
