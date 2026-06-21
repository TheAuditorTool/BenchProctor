# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import jsonify
import importlib
import sys


def BenchmarkTest33651(path_param):
    path_value = path_param
    data = unquote(path_value)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = '/var/app/data/' + data
    sys.path.insert(0, '/opt/app/plugins')
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
