# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest79321():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % (header_value,)
    db.execute('UPDATE users SET name = ?', (str(data),))
    return jsonify({"result": "success"})
