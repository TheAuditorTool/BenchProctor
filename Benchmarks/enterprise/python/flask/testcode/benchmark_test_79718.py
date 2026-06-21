# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest79718():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
