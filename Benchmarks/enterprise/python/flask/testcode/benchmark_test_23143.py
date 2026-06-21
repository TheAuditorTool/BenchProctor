# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest23143():
    upload_name = request.files['upload'].filename
    data = coalesce_blank(upload_name)
    if os.environ.get("APP_ENV", "production") != "test":
        eval(str(data))
    return jsonify({"result": "success"})
