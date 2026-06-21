# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest60948():
    env_value = os.environ.get('USER_INPUT', '')
    with open('/var/app/data/' + str(env_value), 'r') as fh:
        content = fh.read()
    return content
