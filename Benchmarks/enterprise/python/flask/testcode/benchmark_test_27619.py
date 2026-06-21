# SPDX-License-Identifier: Apache-2.0
import subprocess
import shlex
from flask import request, jsonify


def BenchmarkTest27619():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '%s' % (forwarded_ip,)
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
