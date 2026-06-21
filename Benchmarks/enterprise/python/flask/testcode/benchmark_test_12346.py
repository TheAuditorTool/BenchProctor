# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os


def BenchmarkTest12346(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
