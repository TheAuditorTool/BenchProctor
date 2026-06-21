# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest34552():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
