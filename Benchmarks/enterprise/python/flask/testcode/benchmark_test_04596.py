# SPDX-License-Identifier: Apache-2.0
import os
import json


def BenchmarkTest04596():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
