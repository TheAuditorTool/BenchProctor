# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest75287():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return jsonify({"result": "success"})
