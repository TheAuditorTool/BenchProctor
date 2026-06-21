# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest14298():
    raw_body = request.get_data(as_text=True)
    try:
        os.setuid(int(str(raw_body)) if str(raw_body).isdigit() else 65534)
    except OSError:
        pass
    return jsonify({"result": "success"})
