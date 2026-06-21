# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest74141():
    upload_name = request.files['doc'].filename
    data = upload_name if upload_name else 'default'
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    os.unlink(checked_path)
    return jsonify({"result": "success"})
