# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest43711(request: Request):
    referer_value = request.headers.get('referer', '')
    pending = list(str(referer_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
