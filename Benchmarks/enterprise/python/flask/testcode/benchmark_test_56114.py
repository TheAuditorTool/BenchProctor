# SPDX-License-Identifier: Apache-2.0
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest56114():
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
