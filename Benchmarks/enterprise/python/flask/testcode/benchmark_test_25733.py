# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest25733():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    os.remove(str(data))
    return jsonify({"result": "success"})
