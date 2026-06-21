# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest56054():
    upload_name = request.files['upload'].filename
    data = to_text(upload_name)
    if not re.fullmatch("^[\\w\\s.'\\\\;_/\\-]+$", data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return jsonify({"result": "success"})
