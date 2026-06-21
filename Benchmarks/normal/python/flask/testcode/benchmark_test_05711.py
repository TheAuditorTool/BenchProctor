# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest05711():
    raw_body = request.get_data(as_text=True)
    data = default_blank(raw_body)
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return jsonify({"result": "success"})
