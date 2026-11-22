# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

router = APIRouter()


@router.post("/enrich_report")
async def enrich_report(request: Request):
    excerpt = (await request.body()).decode('utf-8')
    reader = make_reader(excerpt)
    cohort = reader()
    subprocess.run('echo ' + str(cohort), shell=True)
    return {"updated": True}
