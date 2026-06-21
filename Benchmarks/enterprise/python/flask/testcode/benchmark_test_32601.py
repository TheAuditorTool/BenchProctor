# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest32601():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
