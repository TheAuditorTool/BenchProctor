# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest31790():
    xml_value = request.get_data(as_text=True)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(xml_value),))
    return jsonify({"result": "success"})
