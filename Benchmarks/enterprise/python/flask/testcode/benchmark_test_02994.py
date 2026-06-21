# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest02994(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
