# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest67760():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
