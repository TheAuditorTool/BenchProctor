# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest39128():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
