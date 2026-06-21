# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import importlib
import sys


def BenchmarkTest26061():
    upload_name = request.files['upload'].filename
    data = '{}'.format(upload_name)
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, data))
    if not full_path.startswith(base_dir + os.sep):
        return jsonify({'error': 'forbidden'}), 403
    checked_path = full_path
    sys.path.insert(0, '/opt/app/plugins')
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})
