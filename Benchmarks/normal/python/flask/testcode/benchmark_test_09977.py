# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
from types import SimpleNamespace


def BenchmarkTest09977():
    user_id = request.args.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    _ev = {}
    eval(compile("_ev['r'] = Markup('<div>' + str(data) + '</div>')", '<sink>', 'exec'))
    return _ev['r']
