# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest49614():
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    return str(data), 200, {'Content-Type': 'text/html'}
