# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest55490():
    upload_name = request.files['upload'].filename
    data = '%s' % (upload_name,)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
