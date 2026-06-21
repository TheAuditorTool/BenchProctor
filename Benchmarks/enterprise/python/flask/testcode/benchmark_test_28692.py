# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest28692():
    xml_value = request.get_data(as_text=True)
    db.execute('SELECT * FROM users WHERE id = ?', (xml_value,))
    return jsonify({"result": "success"})
