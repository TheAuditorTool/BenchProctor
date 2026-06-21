# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import importlib
import sys


def normalise_input(value):
    return value.strip()

def BenchmarkTest67986(path_param):
    path_value = path_param
    data = normalise_input(path_value)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + data
    sys.path.insert(0, '/opt/app/plugins')
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
