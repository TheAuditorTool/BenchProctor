# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest42673():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    return str(data), 200, {'Content-Type': 'text/html'}
