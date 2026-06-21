# SPDX-License-Identifier: Apache-2.0
import os
import unicodedata


def ensure_str(value):
    return str(value)

def BenchmarkTest25089():
    env_value = os.environ.get('USER_INPUT', '')
    data = ensure_str(env_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
