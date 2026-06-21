# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest75893():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    return str(data), 200, {'Content-Type': 'text/html'}
