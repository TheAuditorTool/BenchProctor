# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os


def BenchmarkTest51736(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
