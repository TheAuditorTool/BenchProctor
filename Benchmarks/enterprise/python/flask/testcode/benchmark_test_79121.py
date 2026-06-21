# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest79121():
    user_id = request.args.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
