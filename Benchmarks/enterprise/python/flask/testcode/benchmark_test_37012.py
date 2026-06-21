# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest37012():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    yaml.safe_load(data)
    return jsonify({"result": "success"})
