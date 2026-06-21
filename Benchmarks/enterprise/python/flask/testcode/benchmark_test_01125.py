# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify


def BenchmarkTest01125():
    upload_name = request.files['upload'].filename
    processed = shlex.quote(upload_name)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
