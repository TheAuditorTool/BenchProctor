# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def ensure_str(value):
    return str(value)

def BenchmarkTest59991():
    xml_value = request.get_data(as_text=True)
    data = ensure_str(xml_value)
    _ev = {}
    eval(compile('_ev[\'r\'] = Markup(\'<img src="\' + str(data) + \'">\')', '<sink>', 'exec'))
    return _ev['r']
