# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest71756():
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    return str(data), 200, {'Content-Type': 'text/html'}
