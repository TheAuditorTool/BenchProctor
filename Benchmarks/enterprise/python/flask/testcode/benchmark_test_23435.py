# SPDX-License-Identifier: Apache-2.0
import requests
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest23435():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    _ev = {}
    eval(compile('_ev[\'r\'] = \'<script src="\' + str(data) + \'"></script>\', 200, {\'Content-Type\': \'text/html\'}', '<sink>', 'exec'))
    return _ev['r']
