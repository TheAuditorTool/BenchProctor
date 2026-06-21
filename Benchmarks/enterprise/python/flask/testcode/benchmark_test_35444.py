# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest35444():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '{}'.format(forwarded_ip)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return jsonify({"result": "success"})
