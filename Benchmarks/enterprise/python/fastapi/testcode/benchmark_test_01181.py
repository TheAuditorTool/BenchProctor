# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest01181(request: Request):
    path_value = request.path_params.get('id', '')
    data = default_blank(path_value)
    _ev = {}
    eval(compile("with open('/var/app/data/' + str(data), 'r') as fh:\n    content = fh.read()\n_ev['r'] = content", '<sink>', 'exec'))
    return _ev['r']
