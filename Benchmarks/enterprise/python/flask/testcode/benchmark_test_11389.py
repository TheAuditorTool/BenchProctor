# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os


def BenchmarkTest11389(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
