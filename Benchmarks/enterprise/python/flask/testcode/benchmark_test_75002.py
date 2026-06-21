# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest75002():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % (auth_header,)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
