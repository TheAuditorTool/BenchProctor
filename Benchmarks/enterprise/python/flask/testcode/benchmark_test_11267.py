# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest11267():
    multipart_value = request.form.get('multipart_field', '')
    os.system('echo ' + str(multipart_value))
    return jsonify({"result": "success"})
