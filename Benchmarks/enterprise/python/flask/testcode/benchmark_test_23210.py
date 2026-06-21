# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest23210():
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
