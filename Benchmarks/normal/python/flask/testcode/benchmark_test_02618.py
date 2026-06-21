# SPDX-License-Identifier: Apache-2.0
import os
import unicodedata


def to_text(value):
    return str(value).strip()

def BenchmarkTest02618():
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
