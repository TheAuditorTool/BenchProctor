# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import ast


async def BenchmarkTest64162(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
