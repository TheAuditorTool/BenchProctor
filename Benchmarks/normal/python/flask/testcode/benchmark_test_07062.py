# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest07062():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
