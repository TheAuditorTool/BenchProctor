# SPDX-License-Identifier: Apache-2.0
import os
from types import SimpleNamespace


def BenchmarkTest77957():
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    return str(data), 200, {'Content-Type': 'text/html'}
