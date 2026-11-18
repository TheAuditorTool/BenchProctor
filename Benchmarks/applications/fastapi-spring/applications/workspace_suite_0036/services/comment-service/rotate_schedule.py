# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import PlainTextResponse


router = APIRouter()


@router.post("/rotate_schedule")
async def rotate_schedule(request: Request):
    remark = getattr((await request.form()).get('upload'), 'filename', '')
    if remark:
        synopsis = remark
    else:
        synopsis = ''
    with open('/var/app/data/' + str(synopsis), 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
