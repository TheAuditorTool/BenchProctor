# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest07284(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})
