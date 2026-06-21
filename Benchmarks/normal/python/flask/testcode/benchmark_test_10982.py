# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest10982(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, data))
    if not full_path.startswith(base_dir + os.sep):
        return jsonify({'error': 'forbidden'}), 403
    checked_path = full_path
    os.unlink(checked_path)
    return jsonify({"result": "success"})
