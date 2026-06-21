# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest33439(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    if session.get('role') != 'admin':
        return jsonify({'error': 'forbidden'}), 403
    session['data'] = str(data)
    return jsonify({"result": "success"})
