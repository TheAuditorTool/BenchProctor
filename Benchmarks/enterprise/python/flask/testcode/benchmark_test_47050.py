# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest47050():
    xml_value = request.get_data(as_text=True)
    data = relay_value(xml_value)
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return jsonify({'secret': str(secret)}), 200
