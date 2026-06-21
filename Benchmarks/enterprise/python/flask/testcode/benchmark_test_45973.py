# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest45973():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % (referer_value,)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
