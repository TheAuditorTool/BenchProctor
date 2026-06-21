# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest24597():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
