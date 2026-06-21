# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest33308():
    env_value = os.environ.get('USER_INPUT', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(env_value)
    data = collected
    return str(data), 200, {'Content-Type': 'text/html'}
