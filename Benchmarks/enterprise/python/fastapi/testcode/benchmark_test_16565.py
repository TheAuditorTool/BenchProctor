# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest16565(request: Request):
    stdin_value = input('input: ')
    if stdin_value:
        data = stdin_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
