# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest44821():
    host_value = request.headers.get('Host', '')
    data = coalesce_blank(host_value)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return jsonify({"result": "success"})
