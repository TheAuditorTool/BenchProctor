# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import ast


async def BenchmarkTest76410(request: Request):
    upload_name = (await request.form()).get('upload', '')
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    checked_path = os.path.normpath(data)
    link_path = os.path.join('/var/app/data', str(checked_path))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
