# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest50685():
    env_value = os.environ.get('USER_INPUT', '')
    return '<!-- diagnostic build token: ' + str(env_value) + ' -->', 200, {'Content-Type': 'text/html'}
