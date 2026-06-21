# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest09571():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
