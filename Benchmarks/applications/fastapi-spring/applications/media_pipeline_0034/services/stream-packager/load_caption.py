# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

router = APIRouter()


@router.post("/load_caption")
async def load_caption(request: Request):
    synopsis = (await request.body()).decode('utf-8')
    reader = make_reader(synopsis)
    rendition = reader()
    subprocess.run('echo ' + str(rendition), shell=True)
    return {"updated": True}
