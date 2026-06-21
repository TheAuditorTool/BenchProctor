# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def BenchmarkTest81249():
    multipart_value = request.form.get('multipart_field', '')
    data = '{}'.format(multipart_value)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
