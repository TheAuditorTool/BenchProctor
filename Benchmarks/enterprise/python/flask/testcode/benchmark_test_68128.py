# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest68128():
    referer_value = request.headers.get('Referer', '')
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(referer_value),))
    return jsonify({"result": "success"})
