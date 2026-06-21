# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import importlib
import sys


def coalesce_blank(value):
    return value or ''

def BenchmarkTest20173():
    auth_header = request.headers.get('Authorization', '')
    data = coalesce_blank(auth_header)
    if os.environ.get("APP_ENV", "production") != "test":
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
