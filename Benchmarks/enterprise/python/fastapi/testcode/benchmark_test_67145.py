# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest67145(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    kind = 'json' if str(multipart_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = multipart_value
            data = parsed
        case _:
            data = multipart_value
    request.session['data'] = str(data)
    return {"updated": True}
