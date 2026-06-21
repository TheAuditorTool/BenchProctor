# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest34975():
    upload_name = request.files['upload'].filename
    if upload_name:
        data = upload_name
    else:
        data = ''
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return jsonify({'error': 'file error'}), 500
    return jsonify({"result": "success"})
