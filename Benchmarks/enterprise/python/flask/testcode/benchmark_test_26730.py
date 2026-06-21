# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest26730(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return jsonify({"result": "success"})
