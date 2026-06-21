# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from types import SimpleNamespace


def BenchmarkTest50583(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    processed = str(data).replace("<script", "")
    return Markup('<div>' + str(processed) + '</div>')
