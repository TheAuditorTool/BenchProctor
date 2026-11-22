# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import PlainTextResponse


router = APIRouter()


@router.post("/summarize_index")
async def summarize_index(request: Request):
    paragraph = (await request.body()).decode('utf-8')
    persona = f'{paragraph!s}'
    with open('/var/app/data/' + str(persona), 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
