# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest51776():
    user_id = request.args.get('id', '')
    data = '%s' % (user_id,)
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
