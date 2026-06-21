# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest06882():
    multipart_value = request.form.get('multipart_field', '')
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(multipart_value),))
    return jsonify({"result": "success"})
