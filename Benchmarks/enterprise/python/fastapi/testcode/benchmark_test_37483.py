# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest37483(request: Request, field: str = Form('')):
    field_value = field
    data = coalesce_blank(field_value)
    _ev = {}
    eval(compile("with open('/var/app/data/' + str(data), 'r') as fh:\n    content = fh.read()\n_ev['r'] = content", '<sink>', 'exec'))
    return _ev['r']
