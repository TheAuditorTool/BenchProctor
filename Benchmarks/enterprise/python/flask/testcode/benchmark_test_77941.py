# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest77941():
    upload_name = request.files['upload'].filename
    data = coalesce_blank(upload_name)
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return jsonify({"result": "success"})
