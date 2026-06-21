# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import urllib.parse
from types import SimpleNamespace


def BenchmarkTest72181(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
