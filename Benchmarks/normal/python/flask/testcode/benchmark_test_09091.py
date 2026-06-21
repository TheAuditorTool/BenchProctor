# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest09091():
    xml_value = request.get_data(as_text=True)
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(xml_value)))
    return jsonify({"result": "success"})
