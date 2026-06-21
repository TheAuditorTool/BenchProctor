# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
import os
from types import SimpleNamespace


def BenchmarkTest59778():
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
