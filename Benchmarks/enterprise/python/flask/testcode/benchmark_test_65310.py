# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def BenchmarkTest65310():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
