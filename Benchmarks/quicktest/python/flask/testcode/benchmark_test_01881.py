# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify
import ast


_shared_counter_lock = threading.Lock()

def BenchmarkTest01881():
    upload_name = request.files['upload'].filename
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
