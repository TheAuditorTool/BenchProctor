# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request
from types import SimpleNamespace


def BenchmarkTest17178():
    origin_value = request.headers.get('Origin', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    _ev = {}
    eval(compile('_ev[\'r\'] = \'<script src="\' + str(data) + \'"></script>\', 200, {\'Content-Type\': \'text/html\'}', '<sink>', 'exec'))
    return _ev['r']
