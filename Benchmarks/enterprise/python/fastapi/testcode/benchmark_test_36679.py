# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest36679(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    pending = list(str(xml_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return HTMLResponse('<div>' + str(data) + '</div>')
