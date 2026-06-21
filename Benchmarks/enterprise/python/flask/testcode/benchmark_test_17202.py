# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest17202():
    header_value = request.headers.get('X-Custom-Header', '')
    data = handle(header_value)
    _ev = {}
    eval(compile('_ev[\'r\'] = \'<script src="\' + str(data) + \'"></script>\', 200, {\'Content-Type\': \'text/html\'}', '<sink>', 'exec'))
    return _ev['r']
