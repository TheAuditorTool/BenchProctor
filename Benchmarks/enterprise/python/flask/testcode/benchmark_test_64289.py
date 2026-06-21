# SPDX-License-Identifier: Apache-2.0
from flask import request


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest64289():
    xml_value = request.get_data(as_text=True)
    data = default_blank(xml_value)
    _ev = {}
    eval(compile("with open('/var/app/data/' + str(data), 'r') as fh:\n    content = fh.read()\n_ev['r'] = content", '<sink>', 'exec'))
    return _ev['r']
