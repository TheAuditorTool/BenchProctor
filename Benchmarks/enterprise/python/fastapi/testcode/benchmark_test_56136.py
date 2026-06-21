# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast
import pickle


async def BenchmarkTest56136(request: Request):
    user_id = request.query_params.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    eval(compile("pickle.loads(data.encode('latin-1'))", '<sink>', 'exec'))
    return {"updated": True}
