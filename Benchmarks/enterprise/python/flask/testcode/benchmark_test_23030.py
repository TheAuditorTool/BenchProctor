# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def to_text(value):
    return str(value).strip()

def BenchmarkTest23030():
    user_id = request.args.get('id', '')
    data = to_text(user_id)
    if os.environ.get("APP_ENV", "production") != "test":
        subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
