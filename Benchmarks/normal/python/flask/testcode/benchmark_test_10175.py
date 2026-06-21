# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import jsonify
import os


def BenchmarkTest10175(path_param):
    path_value = path_param
    data = unquote(path_value)
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
