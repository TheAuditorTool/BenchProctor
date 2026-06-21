# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
import ast
import subprocess


async def BenchmarkTest77152(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    try:
        data = str(ast.literal_eval(graphql_var))
    except (ValueError, SyntaxError):
        data = graphql_var
    eval(compile("subprocess.run([str(data), '--status'], shell=False)", '<sink>', 'exec'))
    return {"updated": True}
