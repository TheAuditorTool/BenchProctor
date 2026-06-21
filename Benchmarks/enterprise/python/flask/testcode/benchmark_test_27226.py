# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os


def BenchmarkTest27226(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
