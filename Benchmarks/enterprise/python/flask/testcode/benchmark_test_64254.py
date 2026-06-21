# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest64254():
    multipart_value = request.form.get('multipart_field', '')
    prefix = ''
    data = prefix + str(multipart_value)
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})
