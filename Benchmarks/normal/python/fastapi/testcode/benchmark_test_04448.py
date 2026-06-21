# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import ast
import subprocess


async def BenchmarkTest04448(request: Request):
    upload_name = (await request.form()).get('upload', '')
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    if os.environ.get("APP_ENV", "production") != "test":
        subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
