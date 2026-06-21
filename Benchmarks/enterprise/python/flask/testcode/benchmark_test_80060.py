# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from types import SimpleNamespace


def BenchmarkTest80060(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
