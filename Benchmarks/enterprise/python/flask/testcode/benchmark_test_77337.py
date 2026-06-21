# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest77337():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    if forwarded_ip not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = forwarded_ip
    subprocess.run([str(processed), '--status'], shell=False)
    return jsonify({"result": "success"})
