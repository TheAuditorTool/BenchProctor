# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest44713():
    raw_body = request.get_data(as_text=True)
    data = coalesce_blank(raw_body)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
