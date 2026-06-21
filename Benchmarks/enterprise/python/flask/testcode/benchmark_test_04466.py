# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest04466():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
