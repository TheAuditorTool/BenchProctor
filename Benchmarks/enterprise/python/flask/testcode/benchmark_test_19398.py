# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify


def BenchmarkTest19398():
    multipart_value = request.form.get('multipart_field', '')
    processed = shlex.quote(multipart_value)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
