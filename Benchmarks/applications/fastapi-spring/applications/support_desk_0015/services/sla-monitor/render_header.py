# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/render_header/{id}")
async def render_header(request: Request, id: str):
    phrase = request.path_params.get('id', '')
    grievance, _sep, _rest = str(phrase).partition('\x00')
    subprocess.run(['echo', grievance], shell=False)
    return {"updated": True}
