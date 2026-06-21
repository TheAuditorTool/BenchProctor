# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import shlex
from fastapi import Form


async def BenchmarkTest60568(request: Request, field: str = Form('')):
    field_value = field
    kind = 'json' if str(field_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = field_value
            data = parsed
        case _:
            data = field_value
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
