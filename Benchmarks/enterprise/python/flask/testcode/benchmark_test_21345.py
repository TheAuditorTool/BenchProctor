# SPDX-License-Identifier: Apache-2.0
import requests
import os
import json


def BenchmarkTest21345():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
