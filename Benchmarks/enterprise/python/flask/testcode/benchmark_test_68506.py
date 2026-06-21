# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request
from types import SimpleNamespace


def BenchmarkTest68506():
    referer_value = request.headers.get('Referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    _ev = {}
    eval(compile("_ev['r'] = render_template_string(data)", '<sink>', 'exec'))
    return _ev['r']
