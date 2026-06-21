# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import importlib
import sys


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest58343(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + data
    sys.path.insert(0, '/opt/app/plugins')
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
