# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import request, jsonify
import subprocess


def relay_value(value):
    return value

def BenchmarkTest13216():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = relay_value(forwarded_ip)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return jsonify({"result": "success"})
