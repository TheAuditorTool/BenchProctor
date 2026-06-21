# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
from app_runtime import db


def BenchmarkTest24028():
    multipart_value = request.form.get('multipart_field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(multipart_value)
    data = collected
    if time.time() > 1000000000:
        db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return jsonify({"result": "success"})
