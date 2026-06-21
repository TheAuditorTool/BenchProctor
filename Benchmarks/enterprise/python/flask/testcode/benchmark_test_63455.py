# SPDX-License-Identifier: Apache-2.0
import os
import unicodedata
from types import SimpleNamespace


def BenchmarkTest63455():
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
