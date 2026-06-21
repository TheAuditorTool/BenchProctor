# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest14267():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data, _sep, _rest = str(json_value).partition('\x00')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return jsonify({"result": "success"})
